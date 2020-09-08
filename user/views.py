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


def loginform(request):
    return render(request, 'user/loginform.html')


def login(request):
    email = request.POST['email']
    password = request.POST['password']

    result = usermodels.fetchone(email, password)
    if result is None:
        return HttpResponseRedirect('/user/loginform?result=fail')

    # login 처리
    request.session['authuser'] = result

    return HttpResponseRedirect('/')


def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/')


def updateform(request):
    no = request.session['authuser']['no']

    # 1. 데이터를 가져오기
    # result = usermodels.fetchonebyno(no)
    # data = {'user': result}

    return render(request, 'user/updateform.html')


def update(request):
    no = request.session['authuser']['no']
    name = request.POST['name']
    email = request.POST['email']

    request.session.authuser = {'no': no, 'name': name, 'email': email}
    # request.session['authuser'] ['name'] = name

    return render(request, 'user/update.html')
