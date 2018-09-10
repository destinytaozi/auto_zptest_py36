from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from aha_test4dj.models import Event
from aha_test4dj.models import Guest
from django.db.models.expressions import RawSQL


def index(request):
    return render(request, 'index.html')


# Create your views here.
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        # if user is not None:
        if username == 'admin' and password == 'admin':
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
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(event_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数 取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内 取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "event_manage.html", {"user": username, "events": contacts})
    # return render(request, 'event_manage.html', {"user": username, "events": event_list})


@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('name', '')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})


@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数 取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内 取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})


@login_required
def search_guest(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('name', '')
    guest_list = Guest.objects.filter(realname__contains=search_name)
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})

@login_required
def sign_index(request,eid):
    event = get_object_or_404(Event,id=eid)
    return render(request,'sign_index.html',{'event':event})


@login_required
def sign_index_action(request,eid):
    event = get_object_or_404(Event,id=eid)
    phone = request.POST.get('phone','')
    print(phone)

    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'phone error.'})

    result = Guest.objects.filter(phone=phone,event_id=eid)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'event id or phone error!'})

    result = Guest.objects.get(phone=phone,event_id=eid)
    all_guest = len(Guest.objects.annotate(all_g=Count('sign')).filter(event_id=eid))
    print(all_guest)
    if result.sign:
        return render(request,'sign_index.html',{'event':event,'hint':'user has sign in.','all_guest':all_guest})
    else:
        Guest.objects.filter(phone=phone,event_id=eid).update(sign='1')
        sign_guest = len(Guest.objects.annotate(sign_g=Count('sign')).filter(event_id=eid,sign=1))
        return render(request,'sign_index.html',{'event':event,'hint':'sign in success!','guest':result,'all_guest':all_guest,'sign_guest':sign_guest})
