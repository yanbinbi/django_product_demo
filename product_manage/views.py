import logging
from django.shortcuts import render, redirect
from product_manage.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from product_manage.forms import EmailRegisterForm, LoginForm, PhoneRegisterForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password

logger = logging.getLogger('product_manage.views')
#首页
def home(request):
    return render(request, "home.html", locals())

# 跳转用户注册页面
def register(request):
    email_register_form = EmailRegisterForm()
    phone_register_form = PhoneRegisterForm()
    return render(request, "register.html", locals())

def email_register(request):
    try:
        if request.method == "POST":
            email_register_form = EmailRegisterForm(request.POST)
            if email_register_form.is_valid():
                user = User.objects.create(email=email_register_form.cleaned_data["email"],
                            password=make_password(email_register_form.cleaned_data["password"]))
                user.save()
                return render(request, "index.html", locals())
            else:
                return render(request, "failure.html", {"reason": email_register_form.errors})
        else:
            email_register_form = EmailRegisterForm()

    except Exception as e:
        logger.error(e)
        print(e)

    return render(request, 'register.html', locals())

def phone_register(request):
    try:
        if request.method == "POST":
            phone_register_form = PhoneRegisterForm(request.POST)
            if phone_register_form.is_valid():
                user = User.objects.create(phone_num=phone_register_form.cleaned_data['phone_num'],
                                           password=phone_register_form.cleaned_data['password'])
                user.save()
                # django指定的登录方式
                user.backend = "django.contrib.auth.backends.ModelBackend"
                login(request, user)
            else:
                return render(request, "failure.html", {"reason": phone_register_form.errors})
        else:
            phone_register_form = PhoneRegisterForm()
    except Exception as e:
        logger.error(e)

    return render(request, 'register.html', locals())

# 登录
def do_login(request):
    try:
        if request.method == "POST":
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 将用户的注册邮箱或手机默认设置为username
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                print("username", username)
                # 采用django自带的验证authenticate
                # 判断获得的username是邮箱还是手机号码
                user = authenticate(email=username, password=password)
                print(user)
                if user is None:
                    user = authenticate(phone=username, password=password)
                # 如果用户存在
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                else:
                    return render(request, 'failure.html', {'reason': '登录验证失败'})
                # 登录成功，页面跳转
                return render(request, "index.html", locals())
            else:
                return render(request, "failure.html", {"reason": login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
        print(e)
    return render(request, "login.html", locals())
