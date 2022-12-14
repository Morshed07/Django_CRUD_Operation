from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.
def Index(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request,'addandshow.html',{'form': fm, 'stu': stud})


    # Delete Function

def Delete_Data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

    # Update Function


def Update_Data(request,id):
    if request.method =="POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()

    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'updatestuinfo.html',{'form': fm})
