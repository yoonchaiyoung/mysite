from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import board.models as boardmodels


def index(request):
    results = boardmodels.fetchlist()
    data = {'boardlist': results}
    return render(request, 'board/index.html', data)

def writeform(request):
    return render(request, 'board/write.html')

def write(request):
    title = request.POST['title']
    content = request.POST['content']
    no = request.session['authuser']['no']

    boardmodels.insert(title, content, no)
    return HttpResponseRedirect('/board')

def view(request):
    boardno = request.GET['no']
    result = boardmodels.fetchone(boardno)

    print(result['title'])
    print(result['content'])
    data = {'board': result}
    print(data)
    return render(request, 'board/view.html', data)
