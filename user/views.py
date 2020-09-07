from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import user.models as usermodels

def joinform(request):
    return render(request, 'user/joinform.html')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')

def join(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']

    usermodels.insert(name, email, password, gender)
    return HttpResponseRedirect('/user/joinsuccess')
