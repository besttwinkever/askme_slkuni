"""
URL configuration for askme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from askme_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.indexController, name='index'),
    path('hot/', views.hotController, name='hot'),
    path('ask/', views.askController, name='ask'),
    path('tag/<str:tag>', views.tagController, name='tag'),
    path('question/<int:questionId>', views.questionController, name='question'),
    path('settings/', views.settingsController, name='settings'),
    path('login/', views.loginController, name='login'),
    path('signup/', views.registerController, name='register'),
    path('logout/', views.logoutController, name='logout'),

    # api methods
    path('api/like', views.likeApiController, name='api_like'),
    path('api/right_answer', views.rightAnswerApiController, name='api_right_answer'),
    path('api/search', views.searchApiController, name='api_search'),

    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
