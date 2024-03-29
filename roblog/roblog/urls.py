"""roblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from blog import views



urlpatterns = [
    path('admin/' , admin.site.urls),
    path('' , views.commentIndex , name = 'index'),
    path('comments/detail/<int:id>' , views.commentsDetail , name ='detail'),
    path('comments/latest' , views.latestComment , name='latest'),
    path('comments/store' , views.storeComment , name='store'),
    path('comments/edit/<int:id>' , views.editComment , name='edit'),
    path('comments/save/<int:id>' , views.saveComment , name='save'),
]
