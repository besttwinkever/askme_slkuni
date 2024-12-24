from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from askme_app.models import Question, Tag, Profile, Answer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from askme_app.forms import *
from askme.settings import CENTRIFUGO_SECRET_KEY, CENTRIFUGO_WS_URL, CENTRIFUGO_API_KEY, CENTRIFUGO_API_URL
import jwt
import time
from cent import Client, PublishRequest
from django.core.cache import cache

def getCentrifugoTokenForUser(userId):
    token = jwt.encode({"sub": "42", "exp": int(time.time()) + 10*60}, CENTRIFUGO_SECRET_KEY, algorithm="HS256")
    return token

def publishToCentrifugo(user, answer):
    client = Client(CENTRIFUGO_API_URL, api_key=CENTRIFUGO_API_KEY)
    request = PublishRequest(channel="question-" + str(answer.question.pk), data={
        'answerId': answer.pk,
        'name': user.first_name,
        'imageUrl': Profile.objects.filter(user=user).first().avatar.url,
        'date': answer.created_at.strftime("%b. %d, %Y, %I:%M %p"),
        'text': answer.text,
        'likes': answer.likes_count
    })
    client.publish(request)

def paginate(questions, request, per_page=5):
    page = 1
    if 'page' in request.GET:
        try:
            page = int(request.GET.get('page'))
        except ValueError:
            pass
    paginator = Paginator(questions, per_page)
    try:
        pageObj = paginator.page(page)
    except EmptyPage or PageNotAnInteger:
        pageObj = paginator.page(1)
    return pageObj

def getDataForView(request, is_hot=False, tag=None, baseUrl=None, question=None, form=None, error=None, centrifugo=None):
    popularProfiles = cache.get('popularProfiles')
    if not popularProfiles:
        print('NO CACHE')
        popularProfiles = Profile.objects.popular()
        cache.set('popularProfiles', popularProfiles, 5)
    
    popularTags = cache.get('popularTags')
    if not popularTags:
        print('NO CACHE (TAGS)')
        popularTags = Tag.objects.popular()
        cache.set('popularTags', popularTags, 5)
    
    data = {
        'meta': {
            'is_hot': is_hot,
            'tag': tag,
            'baseUrl': baseUrl,
        },
        'tags': popularTags,
        'profile': request.user.is_authenticated and Profile.objects.filter(user=request.user).first() or None,
        'popularProfiles': popularProfiles,
        'form': form,
        'error': error
    }
    if baseUrl != None and request != None:
        data['page'] = paginate(Question.objects.with_tag(tag) if tag != None else Question.objects.hot() if is_hot else Question.objects.new(), request)
    if question != None:
        data['question'] = question
    if centrifugo != None:
        data['centrifugo'] = centrifugo
    return data

def indexController(request):
    return render(request, 'index.html', getDataForView(request, baseUrl=reverse('index')))

def hotController(request):
    return render(request, 'index.html', getDataForView(request, is_hot=True, baseUrl=reverse('hot')))

def tagController(request, tag):
    return render(request, 'index.html', getDataForView(request, tag=tag, baseUrl=reverse('tag', kwargs={'tag': tag})))

@login_required()
def askController(request):
    form = AskForm(initial={
        'title': request.GET.get('title', None),
    })
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = Question.objects.createQuestion(request.user, form.cleaned_data)
            if question:
                return redirect('question', questionId=question.pk)
            form.add_error(None, 'Error while creating question')
    return render(request, 'ask.html', getDataForView(request, form=form))

@login_required()
def settingsController(request):
    profile = Profile.objects.filter(user=request.user).first()
    form = SettingsForm(initial={
        'email': request.user.email,
        'displayName': request.user.first_name,
        'avatar': profile.avatar
    })
    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES)
        if form.is_valid():
            if Profile.objects.filter(user__email=form.cleaned_data['email']).exclude(user=request.user).first():
                form.add_error('email', 'Email is already in use')
            elif Profile.objects.filter(user__first_name=form.cleaned_data['displayName']).exclude(user=request.user).first():
                form.add_error('displayName', 'Display name is already in use')
            else:
                request.user.email = form.cleaned_data['email']
                request.user.first_name = form.cleaned_data['displayName']
                request.user.save()

                if form.cleaned_data['avatar']:
                    profile.avatar = form.cleaned_data['avatar']
                    profile.save()

                return redirect('settings')
    return render(request, 'settings.html', getDataForView(request, form=form))

def loginController(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = LoginForm(initial={
        'next': request.GET.get('next', 'index')
    })
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect(form.cleaned_data['next'])
            form.add_error(None, 'Invalid login or password')
    return render(request, 'login.html', getDataForView(request, form=form))

def registerController(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = Profile.objects.createProfile(form.cleaned_data)
            if user:
                login(request, user)
                return redirect('index')
            form.add_error(None, 'User with some of your credentials is already exists')
    return render(request, 'register.html', getDataForView(request, form=form))

@login_required()
def logoutController(request):
    logout(request)
    return redirect('index')

def questionController(request, questionId):
    question = Question.objects.filter(pk=questionId).first()
    if question == None:
        return redirect('index')
    form = AnswerForm()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = question.addAnswer(request.user, form.cleaned_data['text'])
            publishToCentrifugo(request.user, answer)
            return HttpResponseRedirect(f'{reverse("question", kwargs={"questionId": questionId})}#answer-{answer.id}')
    return render(request, 'question.html', getDataForView(request, question=question, form=form, centrifugo={
        'token': getCentrifugoTokenForUser(request.user.is_authenticated and request.user.id or 0),
        'wsUrl': CENTRIFUGO_WS_URL
    }))

@login_required()
def likeApiController(request):
    if request.method == 'POST':
        questionId = request.POST.get('questionId', None)
        answerId = request.POST.get('answerId', None)
        if questionId == None:
            return JsonResponse({
                'error': True,
                'message': 'Question id is required'
            })
        question = Question.objects.filter(pk=questionId).first()
        if not question:
            return JsonResponse({
                'error': True,
                'message': 'Question not found'
            })
        likes = 0
        if answerId:
            answer = Answer.objects.filter(pk=answerId, question=question).first()
            if not answer:
                return JsonResponse({
                    'error': True,
                    'message': 'Answer not found'
                })
            hasMyLike, likes = answer.like(request.user)
        else:
            hasMyLike, likes = question.like(request.user)
        return JsonResponse({
            'error': False,
            'likes': likes,
            'hasMyLike': hasMyLike
        })
    return redirect('index')

@login_required()
def rightAnswerApiController(request):
    if request.method == 'POST':
        answerId = request.POST.get('answerId', None)
        if answerId == None:
            return JsonResponse({
                'error': True,
                'message': 'Answer id is required'
            })
        answer = Answer.objects.filter(pk=answerId).first()
        if not answer:
            return JsonResponse({
                'error': True,
                'message': 'Answer not found'
            })
        if answer.question.author.user != request.user:
            return JsonResponse({
                'error': True,
                'message': 'You are not author of this question'
            })
        rightAnswer = answer.question.answers.filter(is_right=True).first()
        if rightAnswer:
            rightAnswer.is_right = False
            rightAnswer.save()
        answer.is_right = True
        answer.save()
        return JsonResponse({
            'error': False
        })
    return redirect('index')

def searchApiController(request):
    if request.method == 'POST':
        query = request.POST.get('search', None)
        if query == None:
            return JsonResponse({
                'error': True,
                'message': 'Query is required'
            })
        questions = Question.objects.search(query)
        return JsonResponse({
            'error': False,
            'questions': [{
                'id': question.pk,
                'title': question.title,
            } for question in questions]
        })
    return redirect('index')