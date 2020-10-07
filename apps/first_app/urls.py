from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sign_up$', views.sign_up),
    url(r'^add_dog$', views.add_dog),
    url(r'^add_new_dog$', views.add_new_dog),
    url(r'^logout$', views.logout),
    url(r'^dog_added$', views.dog_added),
    url(r'^profile/(?P<dog_id>\d+)$', views.profile),
    url(r'^sign_in$', views.login),
    url(r'^select_dog$', views.select_dog),
    url(r'^edit$', views.edit),
    url(r'^delete/(?P<dog_id>\d+)$', views.delete),
    url(r'^edit_dog/(?P<dog_id>\d+)$', views.edit_dog),
    url(r'^dog_updated/(?P<dog_id>\d+)$', views.dog_updated),


    # UPDATE PERSONAL INFORMATION
    url(r'^personal_information$', views.personal_information),
    url(r'^personal_information_action$', views.personal_information_action),


    # SECOND APP
    url(r'^match$', include('apps.second_app.urls')),
    

]
