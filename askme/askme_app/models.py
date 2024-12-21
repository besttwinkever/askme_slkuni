from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class ProfileManager(models.Manager):
    def popular(self):
        return self.annotate(likes_count=Count('question__questionlike')).order_by('-likes_count')[:10]
    
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
        return self.annotate(questions_count=Count('question')).order_by('-questions_count')[:20]

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

    def __str__(self):
        return self.title
    
    def addAnswer(self, user: User, text: str):
        author = Profile.objects.filter(user=user).first()
        if author:
            return Answer.objects.create(text=text, question=self, author=author)
        return None

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_right = models.BooleanField(default=False)

    @property
    def likes_count(self):
        return self.answerlike_set.count()

    def __str__(self):
        return self.text
    
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