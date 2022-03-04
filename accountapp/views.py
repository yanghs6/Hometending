from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import HometendUser
from django.contrib import auth

# Create your views here.

def signup(request):
    res_data = None
    if request.method =='POST':
        useremail = request.POST.get('useremail')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')
        res_data = {}
        if HometendUser.objects.filter(username=useremail):
            res_data['error']='이미 가입된 아이디(이메일주소)입니다.'
        elif password != re_password:
            res_data['error']='비밀번호가 다릅니다.'
        else:
            user = HometendUser.objects.create_user(username = useremail,
                            email = useremail,
                            password = password,
                            )
            auth.login(request, user)
            
            res_data = {'msg': "회원가입이 완료되었습니다!"}
            
            return render(request, 'account/login.html', res_data)
        return render(request, 'account/signup.html', res_data)
    elif request.method =='GET':
        return render(request, 'account/signup.html', res_data)
    # return render(request, "register.html", context)
