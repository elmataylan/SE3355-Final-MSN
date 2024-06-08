"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from msnappserver import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # URL pattern for index.html
    path('news/', views.news_view, name='news'),  # URL pattern for news.html
    path('search/', views.search_news, name='search_news'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('news/<str:category>/', views.news_category, name='news_category'),
    path('filter_news/<str:category>/', views.filter_news_by_category, name='filter_news_by_category'),

]