# from goldmineApp . models import AdminUser, Roles, Branch, User_Activity_Log
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def fn_Login_User_View(request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin':
            return redirect('dashboard_url')
        return redirect('login_user_url')
    return render(request,'login.html')


def fn_Logout_User_View(request):
    logout(request)
    return redirect('admin_login_url')