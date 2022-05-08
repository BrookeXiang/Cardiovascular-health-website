import uuid
from random import Random

from trans import *
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
import numpy as np
import matplotlib.pyplot as plt
import nw

from hashlib import sha1

from django.contrib import messages

from .models import UserInfo, HealthInformation
from . import user_decorator

from django.core.mail import send_mail


def register(request):
    context = {
        'title': '用户注册',
    }
    return render(request, 'user/register.html', context)


def register_handle(request):
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    confirm_pwd = request.POST.get('confirm_pwd')
    email = request.POST.get('email')

    # 判断两次密码一致性
    if password != confirm_pwd:
        return redirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(password.encode('utf8'))
    encrypted_pwd = s1.hexdigest()

    # 创建对象
    UserInfo.objects.create(u_name=username, u_pwd=encrypted_pwd, u_email=email)
    # 注册成功
    context = {
        'title': '用户登陆',
        'username': username,
    }
    return render(request, 'user/login.html', context)


def register_exist(request):
    username = request.GET.get('uname')
    uemail = request.GET.get('uemail')
    count = UserInfo.objects.filter(u_name=username).count()
    email_count = UserInfo.objects.filter(u_email=uemail).count()
    print(email_count)
    return JsonResponse({'count': count, 'email_count': email_count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {
        'title': '用户登陆',
        'error_name': 0,
        'error_pwd': 0,
        'error_vc': 0,
        'uname': uname,
    }
    return render(request, 'user/login.html', context)


# 验证码显示
def verify_show(request):
    return render(request, 'user/login.html')


def login_handle(request):  # 没有利用ajax提交表单
    # 接受请求信息
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    jizhu = request.POST.get('jizhu', 0)
    vc = request.POST.get('vc')
    verifycode = request.session['verifycode']
    user = UserInfo.objects.filter(u_name=uname)
    if len(user) == 1:  # 判断用户密码并跳转
        s1 = sha1()
        s1.update(upwd.encode('utf8'))
        if s1.hexdigest() == user[0].u_pwd and vc == verifycode and user[0].u_name_passOrfail == True:
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)  # 继承与HttpResponse 在跳转的同时 设置一个cookie值
            # 是否勾选记住用户名，设置cookie
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)  # 设置过期cookie时间，立刻过期
            request.session['user_id'] = user[0].id
            request.session['user_name'] = uname
            request.session['type'] = 'user'
            return red
        elif s1.hexdigest() == user[0].u_pwd and vc != verifycode:
            context = {
                'title': '用户名登陆',
                'error_name': 0,
                'error_pwd': 0,
                'error_vc': 1,
                'uname': uname,
                'upwd': upwd,
                'user': user,
                'vc': vc,
            }
            return render(request, 'user/login.html', context)
        elif user[0].u_name_passOrfail == False:
            messages.success(request, "你的账号存在违规行为，已被封禁。")
            context = {
                'title': '用户名登陆',
                'uname': uname,
                'upwd': upwd,
                'user': user,
                'vc': vc,
            }
            return render(request, 'user/login.html', context)
        else:
            context = {
                'title': '用户名登陆',
                'error_name': 0,
                'error_pwd': 1,
                'error_vc': 1,
                'uname': uname,
                'upwd': upwd,
                'user': user,
                'vc': vc,
            }
            return render(request, 'user/login.html', context)
    else:
        context = {
            'title': '用户名登陆',
            'error_name': 1,
            'error_pwd': 0,
            'error_vc': 0,
            'uname': uname,
            'upwd': upwd,
            'user': user,
            'vc': vc,
        }
        return render(request, 'user/login.html', context)


def logout(request):  # 用户登出
    request.session.flush()  # 清空当前用户所有session
    return redirect(reverse("user:index"))


# 修改密码
# 随机生成验证码
def random_str(randomlength=8):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


# 发送邮件重置密码
def findpwdView(request):
    context = {
        'title': '重置密码',
    }
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        print("username:%s" % (username))
        if username == '' or email == '':
            messages.success(request, "请输入用户名和邮箱！")
            return render(request, "user/change_password1.html", context)
        user = UserInfo.objects.get(u_name=username)
        context = {
            'title': '重置密码',
            'user': user,
        }
        if user.uemail == email:
            email_title = "健康管理系统-重置密码"
            code = random_str()  # 随机生成的验证码
            request.session["code"] = code  # 将验证码保存到session
            email_body = "您的密码已重置，为了您的账号安全，请勿将密码泄露。新的密码为：{0}".format(code)
            # send_mail的参数分别是 邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
            send_status = send_mail(email_title, email_body, 'woaisilaowu@163.com', [email], fail_silently=False)
            code = request.session["code"]  # 获取传递过来的验证码
            # 密码加密
            s1 = sha1()
            s1.update(code.encode('utf8'))
            encrypted_pwd = s1.hexdigest()
            user.upwd = encrypted_pwd
            user.save()
            del request.session["code"]  # 删除session
            messages.success(request, "密码已重置，请登录邮箱接受重置密码！")
        else:
            messages.success(request, "用户邮箱与输入邮件不匹配，重置失败！")

        return render(request, "user/change_password1.html", context)
    return render(request, "user/change_password1.html", context)


def index(request):
    # 查询各个分类的最新4条，最热4条数据
    if request.session.get('type') != 'user':
        return redirect(reverse("user:login"))
    username = request.session.get('user_name')
    user = UserInfo.objects.filter(u_name=username).first()

    # 展示回复消息
    # persons1=Information.objects.filter(cusername=cusername).values('cusername1').distinct().order_by('cusername1')

    context = {
        'title': '首页',
    }

    return render(request, 'user/index.html', context)


def form(request):
    message = ""
    if request.session.get('type') != 'user':
        return redirect(reverse("user:login"))
    username = request.session.get('user_name')
    user = UserInfo.objects.filter(u_name=username).first()
    uage = request.POST.get('age')
    usex = request.POST.get('select1')
    stature = request.POST.get('stature')
    uweight = request.POST.get('weight')
    usystolicpress = request.POST.get('systolicpress')
    udiastolicpress = request.POST.get('diastolicpress')
    ucholesterol = request.POST.get('cholesterol')
    ubloodglucose = request.POST.get('bloodglucose')
    usmoke = request.POST.get('select2')
    udrink = request.POST.get('select3')
    usport = request.POST.get('select4')
    message = []
    if uage == '':
        message.append("please input age")
    print('----------------------------')
    print(usex)
    print('----------------------------')
    if usex == '--select--':
        message.append("please input sex;")
    if stature == '':
        message.append("please input height;")
    if uweight == '':
        message.append("please input weight; ")
    if usystolicpress == '':
        message.append("please input stolicpress; ")
    if udiastolicpress == '':
        message.append("please input diastolicpress;")
    if ucholesterol == '':
        ucholesterol = '0'
    if ubloodglucose == '':
        ubloodglucose = '0'
    if usmoke == '--select--':
        message.append("please check whether smoking;")
    if udrink == '- select--':
        message.append("please check whether drink;")
    if usport == '--select--':
        message.append("please check whether sports;")
    if len(message) == 0:
        if isInter(uage) == False:
            message.append("age must be interger number;")
        if isFloat(stature) == False:
            message.append("statur must be number;")
        if isFloat(uweight) == False:
            message.append("weight must be number;")
        if isFloat(usystolicpress) == False:
            message.append("systolicpress must be number")
        if isFloat(udiastolicpress) == False:
            message.append("diastolicpress must be number;")
        if isFloat(udiastolicpress) == False:
            message.append("diastolicpress must be number")
        if isFloat(ubloodglucose) == False:
            message.append("bloodglucose must be number")

    if len(message) == 0:
        print(message)
        info = HealthInformation.objects.create(i_user=user)
        info.i_age = int(uage)
        info.i_sex = int(usex)
        info.i_statur = float(stature)
        info.i_weight = float(uweight)
        info.i_systolicpress = float(usystolicpress)
        info.i_diastolicpress = float(udiastolicpress)
        info.i_cholesterol = float(ucholesterol)
        info.i_bloodglucose = float(ubloodglucose)
        info.i_drink = int(udrink)
        info.i_smoke = int(usmoke)
        info.i_sport = int(usport)
        info.save()
        context = {
            'title': 'index',
            'message_text': 'submit success',
            'message': message
        }

        return render(request, 'user/form.html', context)

    else:
        context = {
            'title': 'index',
            'message_text': 'submilt failed',
            'message': message
        }

        return render(request, 'user/form.html', context)


def figure(request):
    username = request.session.get('user_name')
    healthinfo = HealthInformation.objects.filter(i_user__u_name=username).order_by('-i_time')
    cishu = []
    tall = []
    weight = []
    shousuo = []
    shuzhang = []

    for i, info in enumerate(healthinfo):
        cishu.append(i + 1)
        tall.insert(0, float(info.i_statur))
        weight.insert(0, float(info.i_weight))
        shousuo.insert(0, float(info.i_systolicpress))
        shuzhang.insert(0, float(info.i_diastolicpress))
        if i == 11:
            break

    plt.figure()
    for i in range(len(cishu)):
        plt.annotate(str(tall[i]), xy=(cishu[i], tall[i]), xytext=(cishu[i], tall[i] + 0.05))
    plt.plot(cishu, tall, marker='*', color='b', label='height')

    plt.legend()

    plt.xlabel('num')
    plt.xticks(cishu)

    plt.ylabel('value')

    plt.savefig('./static/images/image.png')

    plt.figure()
    for i in range(len(cishu)):
        plt.annotate(str(tall[i]), xy=(cishu[i], weight[i]), xytext=(cishu[i], weight[i] + 0.05))
    plt.plot(cishu, weight, marker='*', color='b', label='weight')

    plt.legend()

    plt.xlabel('num')
    plt.xticks(cishu)

    plt.ylabel('value')
    plt.savefig('./static/images/image1.png')

    plt.figure()
    for i in range(len(cishu)):
        plt.annotate(str(tall[i]), xy=(cishu[i], shousuo[i]), xytext=(cishu[i], shousuo[i] + 0.05))
    plt.plot(cishu, shousuo, marker='*', color='b', label='systolicpress')
    plt.plot([1, max(cishu)], [90, 90], label='low')
    plt.plot([1, max(cishu)], [140, 140], label='Possible hypertension')

    plt.legend()
    plt.xlabel('num')
    plt.xticks(cishu)

    plt.ylabel('value')
    plt.savefig('./static/images/image2.png')

    plt.figure()
    for i in range(len(cishu)):
        plt.annotate(str(tall[i]), xy=(cishu[i], shuzhang[i]), xytext=(cishu[i], shuzhang[i] + 0.05))
    plt.plot(cishu, shuzhang, marker='*', color='b', label='diastolicpress')
    plt.plot([1, max(cishu)], [60, 60], label='low')
    plt.plot([1, max(cishu)], [90, 90], label='Possible hypertension')

    plt.legend()

    plt.xlabel('num')
    plt.xticks(cishu)

    plt.ylabel('value')
    plt.savefig('./static/images/image3.png')

    context = {
        'title': 'title',
        'error_name': 1,
        'error_pwd': 0,
        'error_vc': 0,
        'tall': tall,
        'weight': weight,
        'shuosuo': shousuo,
        'shuzhang': shuzhang,
    }
    return render(request, 'user/figure.html', context)


def predict(request):
    list = []
    if request.session.get('type') != 'user':
        return redirect(reverse("user:login"))
    username = request.session.get('user_name')
    user = UserInfo.objects.filter(u_name=username).first()
    healthinfo = HealthInformation.objects.filter(i_user__u_name=username).order_by('-i_time').first()
    if healthinfo == None:
        context = {
            'message': 'please submit information',
        }
        return render(request, 'user/predict.html', context)
    else:
        list.append(1)
        list.append(float(healthinfo.i_age))
        list.append(float(healthinfo.i_sex))
        list.append(float(healthinfo.i_statur))
        list.append(float(healthinfo.i_weight))
        list.append(float(healthinfo.i_systolicpress))
        list.append(float(healthinfo.i_diastolicpress))
        if float(healthinfo.i_cholesterol) > 10:
            list.append(1)
        else:
            list.append(0)
        if float(healthinfo.i_bloodglucose) > 10:
            list.append(1)
        else:
            list.append(0)
        list.append(float(healthinfo.i_smoke))
        list.append(float(healthinfo.i_drink))
        list.append(float(healthinfo.i_sport))

    result = nw.predict(list)
    bim = float(healthinfo.i_weight) / (float(healthinfo.i_statur / 100) * float(healthinfo.i_statur / 100))

    bimt = ""
    if bim > 25 or bim < 18.5:
        bimt = ("Your BMI is in the abnormal range,suitable for your weight: " + str("{:0.2f}kg"
                                                                                     ) + "-" + str("{:0.2f}kg")).format(
            18.5 * (float(healthinfo.i_statur / 100) * float(healthinfo.i_statur / 100)),
            25 * (float(healthinfo.i_statur / 100) * float(healthinfo.i_statur / 100)))

    else:
        bimt = "Your BMI is in the normal range"

    if result == False:
        context = {
            'xueya': "Your systolic pressure is " +
                     str(float(healthinfo.i_systolicpress))
                     + "(Normal lower than 140 mmHg)  and your diastolic pressure is "
                     + str(float(healthinfo.i_diastolicpress)) +
                     "(Normal lower than 90 mmHg)",
            'bim': "{:0.2f}".format(bim),
            "bimt": bimt,
            'message': 'you are at high risk and a full medical examination is recommended',
        }
        return render(request, 'user/predict.html', context)
    else:
        context = {
            'xueya': "Your systolic pressure is " +
                     str(float(healthinfo.i_systolicpress))
                     + "(Normal lower than 140 mmHg)  and your diastolic pressure is "
                     + str(float(healthinfo.i_diastolicpress)) +
                     "(Normal lower than 90 mmHg)",
            'bim': "{:0.2f}".format(bim),
            "bimt": bimt,
            'message': 'Congratulations, you are at low risk',
        }
        return render(request, 'user/predict.html', context)
