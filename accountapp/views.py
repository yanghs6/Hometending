from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import HometendUser
from django.contrib import auth

# Create your views here.

def signup(request):
    res_data = None
    if request.method =='POST':
        useremail = request.POST.get('useremail')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')
        res_data = {}
        
        if HometendUser.objects.filter(username=useremail):
            res_data['error']='이미 가입된 아이디(이메일주소)입니다.'
        elif password != re_password:
            res_data['error']='비밀번호가 다릅니다.'
        elif HometendUser.objects.filter(first_name=first_name):
            res_data['error']='동일한 닉네임이 존재합니다.'
        elif len(first_name) > 8:
            res_data['error']='닉네임 길이가 너무 깁니다.'
        else:
            user = HometendUser.objects.create_user(username = useremail,
                            first_name = first_name,
                            email = useremail,
                            password = password,
                            )
            
            user.save()
            
            res_data = {'msg': "회원가입이 완료되었습니다!"}
            
            return render(request, 'account/login.html', res_data)
        
    return render(request, 'account/signup.html', res_data)
