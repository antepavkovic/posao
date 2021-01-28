from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.shortcuts import render,get_object_or_404,redirect
from .models import Main
from proizvod.models import Proizvod
from profil.models import Profil
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=="POST":
        utxt=request.POST.get("username")
        ptxt=request.POST.get("password")
        if utxt != "" and ptxt != "":
            user=auth.authenticate(username=utxt,password=ptxt)
            if user!=None:
                auth.login(request,user)
                return redirect('proizvod')
    return render(request,'login.html')

def mylogout(request):
    logout(request)

    return redirect('home')

def editiranje_proizvoda(request,pk):

    if not request.user.is_authenticated:
        return redirect('login')

    proizvod = Proizvod.objects.filter(pk=pk)
    if request.method=="POST":
        ime_proizvoda=request.POST.get("ime_proizvoda")
        kategorija_proizvoda=request.POST.get("kategorija_proizvoda")
        b=Proizvod.objects.get(pk=pk)
        b.ime_proizvoda=ime_proizvoda
        b.kategorija_proizvoda=kategorija_proizvoda
        b.save()
        return redirect('proizvod')
    return render(request, 'editiranje_proizvoda.html',{'pk':pk,'proizvod':proizvod})


def dodavanje_proizvoda(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        ime_proizvoda=request.POST.get("ime_proizvoda")
        kategorija_proizvoda=request.POST.get("kategorija_proizvoda")
        b=Proizvod(ime_proizvoda=ime_proizvoda,kategorija_proizvoda=kategorija_proizvoda)
        b.save()
        return  redirect('proizvod')

    return render(request, 'dodavanje_proizvoda.html')




def registracija(request):
    main = Main.objects.all()
    if request.method=="POST":
        ime=request.POST.get("ime")
        prezime=request.POST.get("prezime")
        naziv_opga=request.POST.get("naziv_opga")
        adresa=request.POST.get("adresa")
        telefon=request.POST.get("telefon")
        email=request.POST.get("email")
        potvrda_emaila=request.POST.get("potvrda_emaila")
        lozinka=request.POST.get("lozinka")
        if lozinka!="" and email!=0:

            user=User.objects.create_user(username=email,password=lozinka)
            user.save()

            b = Main(ime=ime,prezime=prezime,naziv_opga=naziv_opga,adresa=adresa,telefon=telefon
                      ,email=email,potvrda_emaila=potvrda_emaila,lozinka=lozinka)
            b.save()
            return redirect("login")


    return render(request, 'registracija.html',{"main":main})

