from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView


class HomeNews()

# Create your views here.
def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news':news,
 'categories': categories, 'category': category})

def test(request):
    return HttpResponse('<h1>тестовая страница</h1>')

def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request,'news/view_news.html',{'news_item':news_item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form':form})

def link_page(request):
    return render(request, 'news/link.html')

