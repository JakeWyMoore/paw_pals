from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    # url(r'^dislike/(?P<dog_id>\d+)$', views.dislike),
    # url(r'^like/(?P<dog_id>\d+)$', views.like),
    url(r'^message/(?P<dog_id>\d+)$', views.message),


]