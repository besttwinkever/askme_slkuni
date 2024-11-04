from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .questions import getHotQuestions, getQuestionsContainingTag, getTagListFromQuestions, getAllQuestions, getMostPopularUsers, findQuestionById

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

def indexController(request):
    return render(request, 'index.html', {
        'meta': {
            'is_hot': False,
            'tag': None,
            'baseUrl': reverse('index'),
        },
        'page': paginate(getAllQuestions(), request),
        'tags': getTagListFromQuestions(),
        'popularUsers': getMostPopularUsers(),
        'user': {
            'displayName': 'YourOnlyViewer',
            'image': '/img/default-avatar.png'
        }
    })

def hotController(request):
    return render(request, 'index.html', {
        'meta': {
            'is_hot': True,
            'tag': None,
            'baseUrl': reverse('hot')
        },
        'page': paginate(getHotQuestions(), request),
        'tags': getTagListFromQuestions(),
        'popularUsers': getMostPopularUsers(),
        'user': {
            'displayName': 'YourOnlyViewer',
            'image': '/img/default-avatar.png'
        }
    })

def tagController(request, tag):
    return render(request, 'index.html', {
        'meta': {
            'is_hot': False,
            'tag': tag,
            'baseUrl': reverse('tag', kwargs={'tag': tag})
        },
        'page': paginate(getQuestionsContainingTag(tag), request),
        'tags': getTagListFromQuestions(),
        'popularUsers': getMostPopularUsers(),
        'user': {
            'displayName': 'YourOnlyViewer',
            'image': '/img/default-avatar.png'
        }
    })

def askController(request):
    return render(request, 'ask.html', {
        'tags': getTagListFromQuestions(),
        'popularUsers': getMostPopularUsers(),
        'user': {
            'displayName': 'YourOnlyViewer',
            'image': '/img/default-avatar.png'
        }
    })

def settingsController(request):
    return render(request, 'settings.html', {
        'tags': getTagListFromQuestions(),
        'popularUsers': getMostPopularUsers(),
        'user': {
            'login': 'superuser',
            'email': 'superuser@mail.ru',
            'displayName': 'YourOnlyViewer',
            'image': '/img/default-avatar.png'
        }
    })

def loginController(request):
    return render(request, 'login.html', {
        'tags': getTagListFromQuestions(),
        'popularUsers': getMostPopularUsers(),
        'user': None
    })

def registerController(request):
    return render(request, 'register.html', {
        'tags': getTagListFromQuestions(),
        'popularUsers': getMostPopularUsers(),
        'user': None
    })

def questionController(request, questionId):
    question = findQuestionById(questionId)
    if question == None:
        return redirect('index')
    return render(request, 'question.html', {
        'question': question,
        'tags': getTagListFromQuestions(),
        'popularUsers': getMostPopularUsers(),
        'user': {
            'displayName': 'YourOnlyViewer',
            'image': '/img/default-avatar.png'
        }
    })