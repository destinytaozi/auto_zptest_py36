from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


# Create your views here.
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
            # response = HttpResponseRedirect('/event_manage/')
            # response.session['user']=username
            # return response
        else:
            return render(request, 'index.html', {'error': 'username or password is error!'})


@login_required
def event_manage(request):
    username = request.session.get('user', '')
    return render(request, 'event_manage.html', {"user": username})
