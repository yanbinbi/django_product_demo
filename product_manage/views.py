import logging
from django.shortcuts import render, redirect, HttpResponse
from product_manage.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from product_manage.forms import EmailRegisterForm, LoginForm, PhoneRegisterForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password, check_password
from product_manage.models import User, Product, Cart
from django.template.loader import get_template
from django.template import RequestContext

logger = logging.getLogger('product_manage.views')
#首页
def home(request):
    product_list = Product.objects.all()
    return render(request, "home.html", locals())

# 个人中心
def index(request):
    return render(request, "index.html", locals())

# 跳转用户注册页面
def register(request):
    email_register_form = EmailRegisterForm()
    phone_register_form = PhoneRegisterForm()
    return render(request, "register.html", locals())

# 邮箱注册
def email_register(request):
    try:
        if request.method == "POST":
            email_register_form = EmailRegisterForm(request.POST)
            if email_register_form.is_valid():
                user = User.objects.create(email=email_register_form.cleaned_data["email"],
                                           password=make_password(email_register_form.cleaned_data["password"], 'ybb', 'pbkdf2_sha256'))
                user.save()
                login(request, user)
                return render(request, "index.html", locals())
            else:
                return render(request, "failure.html", {"reason": email_register_form.errors})
        else:
            email_register_form = EmailRegisterForm()

    except Exception as e:
        logger.error(e)
        print(e)

    return render(request, 'register.html', locals())

# 手机注册
def phone_register(request):
    try:
        if request.method == "POST":
            phone_register_form = PhoneRegisterForm(request.POST)
            if phone_register_form.is_valid():
                user = User.objects.create(phone_num=phone_register_form.cleaned_data['phone_num'],
                                           password=phone_register_form.cleaned_data['password'])
                user.save()
                # django指定的登录方式
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

                # 判断获得的username是邮箱还是手机号码
                user = User.objects.filter(email__exact=username, password__exact=make_password(password, 'ybb', 'pbkdf2_sha256'))
                # user = authenticate(request, username=username, password=password)
                if user is None:
                    user = User.objects.filter(phone__exact=username, password__exact=make_password(password, 'ybb', 'pbkdf2_sha256'))
                # 如果用户存在
                if user is not None:
                    # 登录成功，页面跳转到个人中心
                    login(request, user)
                    return render(request, "index.html", locals())
                else:
                    return render(request, 'failure.html', {'reason': '登录验证失败'})
            else:
                return render(request, "failure.html", {"reason": login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
        print(e)
    return render(request, "login.html", locals())

# 注销
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        logger.error(e)

# 商品详情展示
def show_product(request):
    try:
        product_name = request.GET.get("product_name")
        product = Product.objects.filter(product_name=product_name)
        return render(request, "introduction.html", locals())
    except Exception as e:
        logger.error(e)

# 购物车
def shopcart(request):
    cart = request.session.get("cart", None)
    t = get_template("shopcart.html")
    if not cart:
        cart = Cart()
        request.session["cart"] = cart
        c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

