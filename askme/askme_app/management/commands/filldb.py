from django.core.management.base import BaseCommand
from askme_app.models import Profile, Tag, Question, Answer, QuestionLike, AnswerLike, User
import random

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, nargs='?', default=10000)

    def handle(self, *args, **options):

        # Read input arg
        ratio = options['ratio']

        # # Calculate count from ratio
        usersCount = ratio; questionsCount = ratio * 10; answersCount = ratio * 100; tagsCount = ratio; userLikes = ratio * 200
        print(f'Генерируем: {usersCount} пользователей, {questionsCount} вопросов, {answersCount} ответов, {tagsCount} тегов, {userLikes} лайков')

        # Generate tags
        tags = [Tag(name=f'tag{i}') for i in range(tagsCount)]
        Tag.objects.bulk_create(tags)
        print(f'Создано {tagsCount} тегов')

        # Generate profiles
        users = [User(username=f'user{i}', first_name=f'User{i}') for i in range(usersCount)]
        User.objects.bulk_create(users)
        profiles = [Profile(user=user, avatar='cat-avatar.jpeg' if i % 2 else 'default-avatar.png') for i, user in enumerate(users)]
        Profile.objects.bulk_create(profiles)
        print(f'Создано {usersCount} пользователей')

        # Generate questions
        questions = [Question(title=f'Question {i}', text=f'Question text {i}', author=profiles[i % usersCount]) for i in range(questionsCount)]
        Question.objects.bulk_create(questions)

        for question in questions:
            question.tags.set(random.sample(tags, random.randint(1, 5)))
        print(f'Создано {questionsCount} вопросов')

        # Generate answers
        correct_answers = {question.pk: False for question in questions}
        random.shuffle(questions)
        answers = []
        for i in range(answersCount):
            question = questions[i % questionsCount]
            is_right = False
            if not correct_answers[question.pk]:
                is_right = True
                correct_answers[question.pk] = True
            answers.append(Answer(text=f'Answer {i}', question=question, author=profiles[i % usersCount], is_right=is_right))
        Answer.objects.bulk_create(answers)
        print(f'Создано {answersCount} ответов')

        # Generate likes
        questionLikes = []
        question_user_pairs = set()
        while len(questionLikes) < userLikes // 2:
            question = questions[random.randint(0, questionsCount - 1)]
            user = profiles[random.randint(0, usersCount - 1)]
            if (question.pk, user.user.pk) not in question_user_pairs:
                questionLikes.append(QuestionLike(question=question, user=user))
                question_user_pairs.add((question.pk, user.user.pk))
        QuestionLike.objects.bulk_create(questionLikes)
        print('Созданы лайки к вопросам. Создаем лайки к ответам')

        answerLikes = []
        answer_user_pairs = set()
        while len(answerLikes) < userLikes // 2:
            answer = answers[random.randint(0, answersCount - 1)]
            user = profiles[random.randint(0, usersCount - 1)]
            if (answer.pk, user.user.pk) not in answer_user_pairs:
                answerLikes.append(AnswerLike(answer=answer, user=user))
                answer_user_pairs.add((answer.pk, user.user.pk))
        AnswerLike.objects.bulk_create(answerLikes)
        print(f'Создано {userLikes} лайков')