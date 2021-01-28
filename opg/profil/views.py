from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.shortcuts import render,get_object_or_404,redirect
from .models import Profil


def profil():
    pass
def editiranje_profila(request):
    if not request.user.is_authenticated:
        return redirect('login')

    profil = Profil.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        adress = request.POST.get("adress")
        tele = request.POST.get("tele")
        opg_name= request.POST.get("opg_name")
        b = Profil.objects.all()
        b = Profil(name=name, surname=surname,adress=adress,tele=tele,opg_name=opg_name)
        b.save()

        return redirect('pregled_profila')
    return render(request, 'editiranje_profila.html', {'profil': profil})


def pregled_profila(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profil=Profil.objects.all()
    return render(request, 'pregled_profila.html',{"profil":profil})