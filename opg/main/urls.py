from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^mylogout/$', views.mylogout, name='mylogout'),
    url(r'^registracija/$', views.registracija, name='registracija'),
    url(r'^editiranje_proizvoda/(?P<pk>\d+)/$', views.editiranje_proizvoda, name='editiranje_proizvoda'),
    url(r'^proizvod/dodavanje_proizvoda/$', views.dodavanje_proizvoda, name='dodavanje_proizvoda')

]