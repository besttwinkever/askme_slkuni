from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from askme_app.models import Question, Tag, Profile

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

def getDataForView(request=None, is_hot=False, tag=None, baseUrl=None, isAuthenticated=True, question=None):
    data = {
        'meta': {
            'is_hot': is_hot,
            'tag': tag,
            'baseUrl': baseUrl
        },
        'tags': Tag.objects.popular(),
        'profile': isAuthenticated and Profile.objects.first() or None,
        'popularProfiles': Profile.objects.popular()
    }
    if baseUrl != None and request != None:
        data['page'] = paginate(Question.objects.with_tag(tag) if tag != None else Question.objects.hot() if is_hot else Question.objects.new(), request)
    if question != None:
        data['question'] = question
    return data

def indexController(request):
    return render(request, 'index.html', getDataForView(request=request, baseUrl=reverse('index')))

def hotController(request):
    return render(request, 'index.html', getDataForView(request=request, is_hot=True, baseUrl=reverse('hot')))

def tagController(request, tag):
    return render(request, 'index.html', getDataForView(request=request, tag=tag, baseUrl=reverse('tag', kwargs={'tag': tag})))

def askController(request):
    return render(request, 'ask.html', getDataForView())

def settingsController(request):
    return render(request, 'settings.html', getDataForView())

def loginController(request):
    return render(request, 'login.html', getDataForView(isAuthenticated=False))

def registerController(request):
    return render(request, 'register.html', getDataForView(isAuthenticated=False))

def questionController(request, questionId):
    question = Question.objects.filter(pk=questionId).first()
    if question == None:
        return redirect('index')
    return render(request, 'question.html', getDataForView(question=question))