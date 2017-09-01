from django.shortcuts import render, redirect
from product_manage.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from product_manage.forms import EmailRegisterForm, LoginForm, PhoneRegisterForm
from django.contrib.auth import logout, login, authenticate

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
                user = User.objects.create(email=email_register_form.cleaned_data['email'],
                                           password=email_register_form.cleaned_data['password'])
                user.save()
                # django指定的登录方式
                user.backend = "django.contrib.auth.backends.ModelBackend"
                login(request, user)
            else:
                return render(request, "failure.html", {"reason": email_register_form.errors})
        else:
            email_register_form = EmailRegisterForm()
    except:
        pass

    return render(request, 'register.html', locals())

def phone_register(request):
    try:
        if request.method == "POST":
            phone_register_form = PhoneRegisterForm(request.POST)
            if phone_register_form.is_valid():
                user = User.objects.create(email=phone_register_form.cleaned_data['email'],
                                           password=phone_register_form.cleaned_data['password'])
                user.save()
                # django指定的登录方式
                user.backend = "django.contrib.auth.backends.ModelBackend"
                login(request, user)
            else:
                return render(request, "failure.html", {"reason": phone_register_form.errors})
        else:
            phone_register_form = PhoneRegisterForm()
    except:
        pass

    return render(request, 'register.html', locals())