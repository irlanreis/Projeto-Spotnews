from django.shortcuts import get_object_or_404, render, redirect
from news.models import News, Category
from news.forms import CategoryForm, CreateNewsModelForm


def home(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "home.html", context)


def news_detail(request, pk):
    new = get_object_or_404(News, pk=pk)
    all_categories = new.categories.all()
    context = {"new": new, "categories": all_categories}
    return render(request, "news_details.html", context)


def categories_form(request):
    form_instance = CategoryForm()

    if request.method == "POST":
        name = request.POST.get("name")
        Category.objects.create(name=name)
        return redirect("home-page")

    context = {"form": form_instance}
    return render(request, "categories_form.html", context)


def create_news(request):
    form = CreateNewsModelForm()

    if request.method == "POST":
        form = CreateNewsModelForm(request.POST, request.FILES)

        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            form.save_m2m()
            return redirect("home-page")

    context = {"form": form}

    return render(request, "news_form.html", context)
