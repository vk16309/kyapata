from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from . import forms
from django.contrib import messages
from student.filters import ProductFilter
from teacher.models import Teacher,Create,Upvoter

def index(request):
    return render(request, 'index.html', {})

def teacherinst(request):
    return render(request,'teacherinst.html',{})

def login(request):
    return render(request,'login.html',{})


def dashboard(request):
    f = ProductFilter(request.GET , queryset=Teacher.objects.all())
    return render(request, 'dashboard.html', {'filter': f})

def teacherdetail(request,email):
    teacher=get_object_or_404(Teacher, email=email)
    if teacher.class_type=='c':
        ct='Coaching'
    elif teacher.class_type=='t':
        ct='Home Tution'
    else:
        ct='Both Coaching and Home Tution'
    create=get_list_or_404(Create, creater=teacher.teacher)
    return render(request, 'teacherdetail.html', {'teacher':teacher,'create':create,'ctype':ct})

def teacherlist(request):
    return render(request, 'teacherlist.html', {})


def find(request):
    if request.method == "POST":
        form = forms.FindForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.save()
            return redirect(dashboard)
    else:
        form = forms.FindForm()
    return render(request, 'teacherlist.html', {'form': form})


def support(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.save()
            messages.success(request, 'We will help you soon.')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = forms.ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def success(request):
    return render(request,'success.html',{})

def upvote_teacher(request,email):
    current=get_object_or_404(Teacher,email=email)
    done=False
    upvoter_list=get_list_or_404(Upvoter,upvoted=current.teacher)
    for ele in upvoter_list:
        if ele.upvoter==request.user.email:
            done=True
            break
    if not done:
        teacher = get_object_or_404(Teacher,email=email)
        teacher.votes_total+=1
        teacher.save()
        up=Upvoter()
        up.upvoted=teacher.teacher
        up.upvoter=request.user.email
        up.save()
    return redirect(teacherdetail,email)
