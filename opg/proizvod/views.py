from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.shortcuts import render,get_object_or_404,redirect
from .models import Proizvod

def proizvod(request):

    if not request.user.is_authenticated:
        return redirect('login')
    proizvod = Proizvod.objects.all()
    if request.method == "POST":
        ime_proizvoda = request.POST.get("ime_proizvoda")
        kategorija_proizvoda = request.POST.get("kategorija_proizvoda")
        b = Proizvod(ime_proizvoda=ime_proizvoda, kategorija_proizvoda=kategorija_proizvoda)
        b.save()
        return redirect('proizvod')

    return render(request, 'proizvod.html', {'proizvod': proizvod})

def proizvod_delete(request,pk):

    b=Proizvod.objects.get(pk=pk)
    b.delete()

    return redirect('proizvod')
