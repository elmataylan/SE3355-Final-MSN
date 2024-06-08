from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import User1, News1
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

def index(request):
    all_news = News1.objects.all()
    return render(request, 'index.html', {'all_news': all_news})
def news_view(request):
    return render(request, 'news.html')

def filter_news_by_category(request, category):
    news = News1.objects.filter(category=category)
    html = render_to_string('news_items.html', {'news': news})
    return JsonResponse({'html': html})

def search_news(request):
    query = request.GET.get('q')
    if query:
        search_results = News1.objects.filter(header__icontains=query) | News1.objects.filter(text__icontains=query)
    else:
        search_results = News1.objects.none()
    return render(request, 'search_results.html', {'search_results': search_results, 'query': query})


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        country = request.POST.get('country')
        city = request.POST.get('city')


        user = User1(name=name, lastname=lastname, email=email, password=password, country=country, city=city)
        user.save()


        return redirect(reverse('login'))

    return render(request, 'register.html')


def login(request):

    return render(request, 'login.html')



def news_category(request, category):
    news = News1.objects.filter(category=category)
    return render(request, 'news_category.html', {'news': news, 'category': category})