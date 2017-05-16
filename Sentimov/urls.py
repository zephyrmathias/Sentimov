from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^search', views.search, name="search"),
    url(r'^tweet', views.tweet, name="tweet"),
    url(r'^result', views.result, name="result"),
    url(r'^apitweet', views.api_tweet, name="api_tweet"),
    url(r'^delete', views.delete_tweet, name="delete_tweet"),
    url(r'^sentiment', views.sentiment, name="sentiment"),
    url(r'^download', views.download, name="download"),
]
