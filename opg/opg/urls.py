from django.contrib import admin
from django.urls import path
from django.conf.urls import  include,url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('main.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'',include('proizvod.urls')),
    url(r'',include('profil.urls'))

]
