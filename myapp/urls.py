"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="my home page"),
    path('index', views.index ,name="my home page"),
    path('about',views.about,name="about pages"),
    path('Contact',views.Contact, name='Contact'),
    path('course-details',views.course, name='course'),
    path('courses',views.courses, name='courses'),
    path('elements',views.elements, name='courses'),
    path('blog',views.blog, name='courses'),
    path('single-blog',views.blogdetails, name='courses'),
]
