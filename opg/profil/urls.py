from django.conf.urls import url
from . import views


urlpatterns=[
        url(r'^profil/$', views.profil, name='profil'),
        url(r'^pregled_profila/$', views.pregled_profila, name='pregled_profila'),
        url(r'^editiranje_profila/$', views.editiranje_profila, name='editiranje_profila')
]