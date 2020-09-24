from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import board.models as boardmodels


def index(request):
    results = boardmodels.fetchlist()
    # data = {'boardlist': results}
    session_user_no = 0

    try:                                        # 로그인 했으면 flag=True
        session_user_no = request.session['authuser']['no']
        flag = True
    except:                                     # 로그인 안했으면 flag=False
        flag = False
    data = {'boardlist': results, 'flag': flag, 'session_user_no': session_user_no}

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
    boardmodels.updatehit(boardno)              # 조회수 +1
    result = boardmodels.fetchone(boardno)
    session_user_no = 0

    try:
        session_user_no = request.session['authuser']['no']
        flag = True
    except:
        flag = False

    data = {'board': result, 'flag': flag, 'session_user_no': session_user_no}
    return render(request, 'board/view.html', data)

def modifyform(request):
    boardno = request.GET['no']

    result = boardmodels.fetchone(boardno)

    data = {'board': result}
    return render(request, 'board/modify.html', data)

def modify(request):
    title = request.POST['title']
    content = request.POST['content']
    no = request.POST['no']

    boardmodels.update(title, content, no)

    return HttpResponseRedirect('/board/view?no={}'.format(no))

def delete(request):
    no = request.session['authuser']['no']      # 로그인한 사람번호
    board_user_no = request.GET['user_no']      # 게시글의 작성자 번호
    board_no = request.GET['board_no']          # 글 번호

    if no == int(board_user_no):
        boardmodels.delete(board_no)
        return HttpResponseRedirect('/board')
    else:
        return HttpResponseRedirect('/board')
