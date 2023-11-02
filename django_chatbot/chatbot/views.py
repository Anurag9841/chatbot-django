from django.shortcuts import render,redirect
from django.http import JsonResponse
from bardapi import Bard
from django.contrib.auth.models import User,auth
from django.contrib import messages
import os
from .models import Chat
from django.utils import timezone
os.environ["_BARD_API_KEY"] = "cggP5kYz-hYq3KUQtAEPAGBbd2HcXtWO5Fq6CywP51aH90hvarfoAnBoLQ4TC_6OWg7gUw."

def ask_bard(message):
    answer = Bard().get_answer(str(message))['content']
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_bard(message)
        chat = Chat(user=request.user,message=message,response=response,created_at = timezone.now())
        chat.save()
        return JsonResponse({'message':message,'response':response})
    else:
        return render(request,'chatbot.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password1 = request.POST['password2']
        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.warning(request,'email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.warning(request,'user already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.warning(request,'password doesnot match')
            return redirect('register')
    else:
        return  render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'credientials invalid')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')