from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from .models import ElaClass
from .models import ScienceClass
from .models import SocialClass
from .models import MathClass
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "index.html")
@login_required(login_url='home')
def portal(request):
    return render(request, "portal.html")

def signin(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(username=username1, password=password1)

        if user is not None:
            login(request, user)
            return redirect('portal')
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

        return render(request, index.html)
            
def submit(request):
    if request.method == 'POST':
        if(request.POST["English"] == "Write On"):
            if ElaClass.objects.filter(id=1).first().mMembers < ElaClass.objects.filter(id=1).first().maxMembers:
                newMembers = ElaClass.objects.filter(id=1).first().mMembers + 1
                ElaClass.objects.filter(id=1).update(mMembers = newMembers)
        else:
            if ElaClass.objects.filter(id=2).first().mMembers < ElaClass.objects.filter(id=2).first().maxMembers:
                newMembers = ElaClass.objects.filter(id=2).first().mMembers + 1
                ElaClass.objects.filter(id=2).update(mMembers = newMembers)
                print("WhoopS!")
        if(request.POST["Math"] == "Algebra 4"):
            if MathClass.objects.filter(id=1).first().mMembers < MathClass.objects.filter(id=1).first().maxMembers:
                newMembers = MathClass.objects.filter(id=1).first().mMembers + 1
                MathClass.objects.filter(id=1).update(mMembers = newMembers)
        else:
            if MathClass.objects.filter(id=2).first().mMembers < MathClass.objects.filter(id=2).first().maxMembers:
                newMembers = MathClass.objects.filter(id=2).first().mMembers + 1
                MathClass.objects.filter(id=2).update(mMembers = newMembers)
                print("WhoopS!")
        
        if(request.POST["Social"] == "World"):
            print(SocialClass.objects)
            if SocialClass.objects.filter(id=2).first().mMembers < SocialClass.objects.filter(id=2).first().maxMembers:
                newMembers = SocialClass.objects.filter(id=2).first().mMembers + 1
                SocialClass.objects.filter(id=2).update(mMembers = newMembers)
        else:
            print(SocialClass.objects)
            if SocialClass.objects.filter(id=1).first().mMembers < SocialClass.objects.filter(id=1).first().maxMembers:
                newMembers = SocialClass.objects.filter(id=1).first().mMembers + 1
                SocialClass.objects.filter(id=1).update(mMembers = newMembers)
                print("WhoopS!")
        
        if(request.POST["Science"] == "Chem"):
            print(ScienceClass.objects.filter(id=2).first().cName)
            if ScienceClass.objects.filter(id=1).first().mMembers < ScienceClass.objects.filter(id=1).first().maxMembers:
                newMembers = ScienceClass.objects.filter(id=1).first().mMembers + 1
                ScienceClass.objects.filter(id=1).update(mMembers = newMembers)
        else:
            if ScienceClass.objects.filter(id=2).first().mMembers < ScienceClass.objects.filter(id=2).first().maxMembers:
                newMembers = ScienceClass.objects.filter(id=2).first().mMembers + 1
                ScienceClass.objects.filter(id=2).update(mMembers = newMembers)
                print("WhoopS!")
        

        
        return HttpResponseRedirect('home')

        