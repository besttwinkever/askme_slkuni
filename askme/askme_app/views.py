from django.shortcuts import render

def indexController(request):
    return render(request, 'index.html')

def askController(request):
    return render(request, 'ask.html')

def tagController(request):
    return render(request, 'tag.html')

def settingsController(request):
    return render(request, 'settings.html')

def loginController(request):
    return render(request, 'login.html')

def registerController(request):
    return render(request, 'register.html')

def questionController(request):
    return render(request, 'question.html')