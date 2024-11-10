from django.core.management.base import BaseCommand
from askme_app.models import Profile, Tag, Question, Answer, QuestionLike, AnswerLike, User

class Command(BaseCommand):
    def handle(self, *args, **options):
        Profile.objects.all().delete()
        Tag.objects.all().delete()
        Question.objects.all().delete()
        Answer.objects.all().delete()
        QuestionLike.objects.all().delete()
        AnswerLike.objects.all().delete()
        User.objects.all().delete()
        print('База данных очищена')