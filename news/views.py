from django.shortcuts import get_object_or_404, render
from news.models import News


def home(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "home.html", context)


def news_detail(request, pk):
    new = get_object_or_404(News, pk=pk)
    all_categories = new.categories.all()
    context = {"new": new, "categories": all_categories}
    return render(request, "news_details.html", context)
