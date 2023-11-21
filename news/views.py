from django.shortcuts import render
from news.models import News


def home(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "home.html", context)
