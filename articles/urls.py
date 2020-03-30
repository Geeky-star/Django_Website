from django.conf.urls import url 
from articles import views

urlpatterns = [
    url(r'articles/', views.articles, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]

