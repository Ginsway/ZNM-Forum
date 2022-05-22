from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('post-article/', views.post_article, name='post_article')
]
