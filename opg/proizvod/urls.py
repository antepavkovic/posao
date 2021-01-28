from django.conf.urls import url
from . import views


urlpatterns=[
        url(r'^proizvod/$', views.proizvod, name='proizvod'),
        url(r'^proizvod/del/(?P<pk>\d+)/$',views.proizvod_delete,name='proizvod_delete')
]