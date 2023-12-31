"""
URL configuration for trybe_news project.

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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from news import views
from rest_framework.routers import DefaultRouter
from news_rest.views.category_view import CategoryViewSet
from news_rest.views.user_view import UserViewSet
from news_rest.views.news_view import NewsViewSet


router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"users", UserViewSet)
router.register(r"news", NewsViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home-page"),
    path("news/<int:pk>", views.news_detail, name="news-details-page"),
    path("categories", views.categories_form, name="categories-form"),
    path("news", views.create_news, name="news-form"),
    path('api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
