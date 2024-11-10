from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class ProfileManager(models.Manager):
    def popular(self):
        return self.annotate(likes_count=Count('question__questionlike')).order_by('-likes_count')[:10]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default-avartar.png')
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