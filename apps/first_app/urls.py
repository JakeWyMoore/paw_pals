from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sign_up$', views.sign_up),
    url(r'^add_dog$', views.add_dog),
    url(r'^logout$', views.logout),
    url(r'^dog_added$', views.dog_added),
    url(r'^profile/(?P<dog_id>\d+)$', views.profile),
    url(r'^sign_in$', views.login),
    url(r'^select_dog$', views.select_dog),
    url(r'^edit$', views.edit),
    url(r'^delete/(?P<dog_id>\d+)$', views.delete),
    url(r'^edit_dog/(?P<dog_id>\d+)$', views.edit_dog),
    url(r'^dog_updated/(?P<dog_id>\d+)$', views.dog_updated),




    # UPDATE USERNAME
    url(r'^update_username$', views.update_username),
    url(r'^username_action$', views.username_action),

    # UPDATE EMAIL
    url(r'^update_email$', views.update_email),
    url(r'^email_action$', views.email_action),

    # UPDATE PASSWORD
    url(r'^update_password$', views.update_password),
    url(r'^password_action$', views.password_action),


    url(r'^match/', include('apps.second_app.urls')),

]
