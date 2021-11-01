from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
    path('categories/<int:pk>/detail/', views.CategoryView.as_view()),

    path('articles/', views.ArticleView.as_view()),
    path('articles/<int:pk>/detail/', views.ArticleView.as_view()),

    path('commits/', views.CommitView.as_view()),
    path('commits/<int:pk>/detail/', views.CommitView.as_view())
]
