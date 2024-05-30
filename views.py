from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from.forms import *
from .models import *


# Create your views here.
def faculty_logout(request):
    return render(request,'faculty_logout.html')
def c(request):
    return render(request,'c.html')
def div_sem(request):
    return render(request,'div_sem.html')
def div_course(request):
    return render(request,'div_course.html')
def logout(request):
    return render(request,'logout.html')

def index(request):
    return render(request,'index.html')

def admin_s(request):
    return render(request,'admin_s.html')

def Login(request):
    if request.method=='POST':
        data=request.POST
        uname=data.get('username')
        password=data.get('password')
        print(uname,password)
        if not User.objects.filter(username=uname).exists():
            messages.error(request, 'Invalid username')
            return redirect('/admin_s/')

        else:
            u=authenticate(username=uname,password=password)
            print(u)
            if u is None:
                messages.error(request, 'password is Invalid')
                return redirect('/admin_s/')
            else:
                login(request,u)

    return render(request,'login.html')


def login_h(request):
    if request.method== 'POST':
      f=logform(request.POST)
      if f.is_valid():
          print('form is vaild')
          try:
             f.save()

             return render(request,'index.html')
          except:
            pass
      else:
          pass
    else:
        f=logform()
    return render(request, 'login_h.html',{'form':f})

def l_read(request):
    s=user.objects.all()
    context={
        's':s,
    }
    return render(request,'l_read.html',context)

def l_record(request):
    s = user.objects.all()
    context = {
        's': s,
    }
    return render(request, 'l_record.html', context)
def aboutus(request):
    return render(request,'aboutus.html')

def bca(request):
    return render(request,'bca.html')

def feedback_u(request):
    if request.method== 'POST':
      f=feedform(request.POST)
      if f.is_valid():
          print('form is vaild')
          try:
             f.save()

             return render(request,'index.html')
          except:
            pass
      else:
          pass
    else:
        f=feedform()
    return render(request, 'feedback.html',{'form':f})
def f_read(request):
    s=feedback.objects.all()
    context={
        's':s,
    }
    return render(request,'f_read.html',context)

def f_record(request):
    s = feedback.objects.all()
    context = {
        's': s,
    }
    return render(request, 'f_record.html', context)

def create(request):
    if request.method== 'POST':
      f=facform(request.POST)
      if f.is_valid():
          print('form is vaild')
          try:
             f.save()

             return redirect('/faculty_record/')
          except:
            pass
      else:
          pass
    else:
        f=facform()
    return render(request, 'create.html',{'form':f})
def read(request):
    s=facultyform.objects.all()
    context={
        's':s,
    }
    return render(request,'read.html',context)

def faculty_record(request):
    s = facultyform.objects.all()
    context = {
        's': s,
    }
    return render(request, 'faculty_record.html', context)

def Delete(request,id):
    s=facultyform.objects.get(id=id)
    s.delete()
    return redirect('/read/')

def update(request,id):
    s=facultyform.objects.get(id=id)
    if request.method== 'POST':
      f=facform(request.POST,instance=s)
      if f.is_valid():
          print('form is vaild')
          try:
             f.save()
             return redirect('/faculty_record/')
             #return HttpResponse('form is submited')
          except:
            pass
      else:
          pass
    else:
        f=facform()
    return render(request,'update.html',{'s':s,'f':f})

def sem1(request):
    return render(request,'sem1.html')
def sem2(request):
    return render(request,'sem2.html')
def sem3(request):
    return render(request,'sem3.html')
def sem4(request):
    return render(request,'sem4.html')
def sem5(request):
    return render(request,'sem5.html')
def sem6(request):
    return render(request,'sem6.html')



def s_create(request):
    if request.method== 'POST':
      f=subform(request.POST, request.FILES)

      if f.is_valid():

          print('form is vaild')
          try:
             f.save()
             return HttpResponse('submitted')


          except:
            pass
      else:
          pass
    else:
        f=subform()
    return render(request, 's_create.html',{'form':f})

def s_read(request):
    s=subject.objects.all()
    context={
        's':s,
    }
    return render(request,'s_read.html',context)

def Delete_su(request,id):
    s=subject.objects.get(id=id)
    s.delete()
    return redirect('/s_record/')
def Delete_sub(request,id):
    s=subject.objects.get(id=id)
    s.delete()
    return redirect('/f_subject/')

def s_update(request,id):
    s=subject.objects.get(id=id)
    if request.method== 'POST':
      f=subform(request.POST,instance=s)
      if f.is_valid():
          print('form is vaild')
          try:
             f.save()

             return HttpResponse('updated')
          except:
            pass
      else:
          pass
    else:
        f=subform()
    return render(request,'s_update.html',{'s':s,'f':f})

def s_record(request):
    s = subject.objects.all()
    context = {
        's': s,
    }
    return render(request, 's_record.html', context)

def sem_record(request):

    return render(request, 'sem_record.html')


def se_create(request):
    if request.method == 'POST':
        f = semform(request.POST)
        if f.is_valid():
            print('form is vaild')
            try:
                f.save()

                return HttpResponse('submitted')
            except:
                pass
        else:
            pass
    else:
        f = semform()
    return render(request, 'se_create.html', {'form': f})


def se_record(request):
    s = semester.objects.all()
    context = {
        's': s,
    }
    return render(request, 'se_record.html', context)
def Delete_s(request,id):
    s=semester.objects.get(id=id)
    s.delete()
    return redirect('/se_record/')

def Delete_se(request,id):
    s=semester.objects.get(id=id)
    s.delete()
    return redirect('/f_sem/')



def div_create(request):
    if request.method == 'POST':
        f = divform(request.POST)
        if f.is_valid():
            print('form is vaild')
            try:
                f.save()

                return HttpResponse('submitted')
            except:
                pass
        else:
            pass
    else:
        f = divform()
    return render(request, 'div_create.html', {'form': f})


def div_record(request):
    s = division.objects.all()
    context = {
        's': s,
    }
    return render(request, 'div_record.html', context)

def Delete_d(request,id):
    s=division.objects.get(id=id)
    s.delete()
    return redirect('/div_record/')

def Delete_di(request,id):
    s=division.objects.get(id=id)
    s.delete()
    return redirect('/faculty_div2/')

def f_login(request):
    if request.method=='POST':
        data=request.POST
        uname=data.get('username')
        password=data.get('password')
        print(uname,password)
        if not User.objects.filter(username=uname).exists():
            messages.error(request, 'Invalid username')
            return redirect('/faculty_index/')

        else:
            u=authenticate(username=uname,password=password)
            print(u)
            if u is None:
                messages.error(request, 'password is Invalid')
                return redirect('/faculty_index/')
            else:
                login(request,u)

    return render(request,'f_login.html')

def faculty_index(request):
    return render(request,'faculty_index.html')

def f_feedback(request):
    s = feedback.objects.all()
    context = {
        's': s,
    }
    return render(request, 'f_feedback.html', context)
def f_sem(request):
    s = semester.objects.all()
    context = {
        's': s,
    }
    return render(request, 'f_sem.html', context)
def f_student(request):
    s = user.objects.all()
    context = {
        's': s,
    }
    return render(request, 'f_student.html', context)

def f_subject(request):
    s = subject.objects.all()
    context = {
        's': s,
    }
    return render(request, 'f_subject.html', context)

def faculty_login(request):
    if request.method=='POST':
        data=request.POST
        uname=data.get('username')
        password=data.get('password')
        print(uname,password)
        if not User.objects.filter(username=uname).exists():
            messages.error(request, 'Invalid username')
            return redirect('/faculty_index/')

        else:
            u=authenticate(username=uname,password=password)
            print(u)
            if u is None:
                messages.error(request, 'password is Invalid')
                return redirect('/faculty_index/')
            else:
                login(request,u)

    return render(request,'login.html')

def faculty_div1(request):
    return render(request,'faculty_div1.html')
def faculty_div2(request):
    s = division.objects.all()
    context = {
        's': s,
    }
    return render(request, 'faculty_div2.html', context)