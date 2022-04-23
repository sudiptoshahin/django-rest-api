from __future__ import unicode_literals
from api_basic import views
from api_basic.views import ArticleAPIView, ArticleDetailAPIView
from django.urls import path, re_path

urlpatterns = [

    # path('article/', views.article_list, name='article_list'),
    path('article/', ArticleAPIView.as_view(), name='article_list'),

    # path('article/detail/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/detail/<int:pk>/', ArticleDetailAPIView.as_view(), name='article_detail'),
]
