from __future__ import unicode_literals

from django.db import router
from api_basic import views
# from api_basic.views import ArticleDetailAPIView, GenericsAPIView
from api_basic.views import ArticleViewsets
from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewsets, basename='article')

urlpatterns = [

    # path('article/', views.article_list, name='article_list'),
    # path('article/', ArticleAPIView.as_view(), name='article_list'),
    # path('generic/article/', GenericsAPIView.as_view()),
    # path('generic/article/<int:pk>/', GenericsAPIView.as_view()),

    # viewsets
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    # path('article/detail/<int:pk>/', views.article_detail, name='article_detail'),
    # path('article/detail/<int:pk>/', ArticleDetailAPIView.as_view(), name='article_detail'),
]
