from django.conf.urls import url
from django.urls import path, include
from . import views
                    
urlpatterns = [
    url('', views.index),
    url(r'^message/(?P<dog_id>\d+)$', views.message),
    url(r'^message_action$', views.message_action),

    # url(r'^dislike/(?P<dog_id>\d+)$', views.dislike),
    # url(r'^like/(?P<dog_id>\d+)$', views.like),

]