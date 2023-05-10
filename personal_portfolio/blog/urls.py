from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
    path('create/blog', views.create_blog, name="blog_create" ),
    path("create/category", views.create_category, name="category_create")
]
