from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from datetime import datetime, timedelta
from django.db.models import Sum
from django.utils import timezone
from django.db.models import F, Q
from django.db.models import F, Count
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.postgres.search import SearchVector

class ProfileManager(models.Manager):

    # Лучшие пользователи - это 10 пользователей задавших самые популярные вопросы или давших самые популярные ответы за последнюю неделю.
    # Под популярностью подразумевается количество лайков на вопросах и ответах.
    # Данные не должны дублироваться (если у пользователя 5 ответов и 1 лайк на вопрос, то не должно быть 5 лайков, а должен быть 1 лайк)
    def popular(self):
        week_ago = timezone.now() - timedelta(days=7)
        return self.filter(
            Q(answer__created_at__gte=week_ago) | Q(question__created_at__gte=week_ago)
        ).annotate(
            likesCount = Count('answer__answerlike', distinct=True) + Count('question__questionlike', distinct=True)
        ).order_by('-likesCount')[:10]
        
    
    def createProfile(self, data: dict):
        user = User.objects.filter(models.Q(username=data['login']) | models.Q(email=data['email']) | models.Q(first_name=data['displayName'])).first()
        if user:
            return None
        user = User.objects.create_user(username=data['login'], email=data['email'], password=data['password'], first_name=data['displayName'])
        profile = self.create(user=user)
        return user

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default-avatar.png')
    objects: ProfileManager = ProfileManager()

    def __str__(self):
        return self.user.username

class TagManager(models.Manager):
    def popular(self):
        three_months_ago = datetime.now() - timedelta(days=90)
        return self.filter(
            question__created_at__gte=three_months_ago
        ).annotate(
            tagsCount = Count('question__tags', distinct=True)
        ).order_by('-tagsCount')[:10]

class Tag(models.Model):
    name = models.CharField(max_length=255)
    objects: TagManager = TagManager()

    def __str__(self):
        return self.title

class QuestionManager(models.Manager):
    def hot(self):
        return self.annotate(ordered_likes_count=Count('questionlike')).order_by('-ordered_likes_count')
    
    def with_tag(self, tag):
        return self.filter(tags__name=tag)
    
    def new(self):
        return self.order_by('-created_at')
    
    def createQuestion(self, user: User, data: dict):
        question = self.create(title=data['title'], text=data['text'], author=Profile.objects.filter(user=user).first())
        for tag in data['tags']:
            question.tags.add(Tag.objects.get_or_create(name=tag)[0])
        return question
    
    def search(self, query):
        return Question.objects.annotate(
            search = SearchVector('title') + SearchVector('text')
        ).filter(search=query)[:5]
        
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    objects: QuestionManager = QuestionManager()

    @property
    def likes_count(self):
        return self.questionlike_set.count()

    @property
    def answers_count(self):
        return self.answer_set.count()

    @property
    def answers(self):
        return self.answer_set.all()

    @property
    def liked_by_profiles(self):
        return [like.user for like in self.questionlike_set.all()]

    def __str__(self):
        return self.title
    
    def addAnswer(self, user: User, text: str):
        author = Profile.objects.filter(user=user).first()
        if author:
            return Answer.objects.create(text=text, question=self, author=author)
        return None
    
    def like(self, user):
        like, created = QuestionLike.objects.get_or_create(question=self, user=Profile.objects.filter(user=user).first())
        if not created:
            like.delete()
        return (created, self.likes_count)

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_right = models.BooleanField(default=False)

    @property
    def likes_count(self):
        return self.answerlike_set.count()

    @property
    def liked_by_profiles(self):
        return [like.user for like in self.answerlike_set.all()]

    def __str__(self):
        return self.text
    
    def like(self, user):
        like, created = AnswerLike.objects.get_or_create(answer=self, user=Profile.objects.filter(user=user).first())
        if not created:
            like.delete()
        return (created, self.likes_count)
    
class QuestionLike(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('question', 'user')

class AnswerLike(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('answer', 'user')