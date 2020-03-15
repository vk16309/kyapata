from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Teacher,Create,Payment,Upvoter

@login_required(login_url="/accounts/signup")
def personal(request):
    #p = get_object_or_404(Payment,pk=1)
    if request.method=="POST":
        if request.POST['name'] and request.POST['email'] and request.POST['contact'] and request.POST['city'] and request.POST['state']:
            teacher = Teacher()
            up=Upvoter()
            teacher.name = request.POST['name']
            teacher.institute_name = request.POST['institute_name']
            teacher.email = request.POST['email']
            teacher.contact = request.POST['contact']
            teacher.city = request.POST['city']
            teacher.state = request.POST['state']
            teacher.acheivements = request.POST['acheivements']
            teacher.experience = request.POST['experience']
            teacher.videolinks = request.POST['videolinks']
            teacher.image = request.FILES['image']
            teacher.class_type=request.POST['class_type']
            teacher.teacher = request.user
            teacher.save()
            up.upvoted=request.user
            up.save()
            return redirect('payment')


        else:
            return render(request,'teacher/personal.html',{'error':'Something is missing! Try again to fill the form'})
    else:
        return render(request,'teacher/personal.html')

def create(request):
    p = get_object_or_404(Payment,pk=request.user.id)
    if p.premium==request.user and p.status==1:
        if request.method=='POST':
            if request.POST['class_name'] and request.POST['subject']:
                create = Create()
                create.class_name = request.POST['class_name']
                create.subject = request.POST['subject']
                create.creater = request.user
                create.save()
                return redirect('check')
            else:
                return render(request,'teacher/create.html',{'error':'Something is missing! Try again to fill the form'})
        else:
            return render(request,'teacher/create.html')
    else:
        return render(request,'teacher/payment.html')
@login_required(login_url="/accounts/signup")
def dashboard(request,teacher_id):
    teacher = get_object_or_404(Teacher,pk=teacher_id)
    lists = Create.objects
    print(lists)
    print(type(lists))
    list1=[]
    #for c in lists:
    #    if c.creater == teacher.teacher:
    #        list1.append(c)
    return render(request,'teacher/dashboard.html',{'teacher':teacher,'list1':list1})
@login_required(login_url="/accounts/signup")
def create_list(request,create_id):
    create = get_object_or_404(Create,pk=create_id)
    if create.creater == request.user:
        return HttpResponse('OKAY')
@login_required()
def payment(request):
    p = Payment()
    p.id = request.user.id
    if request.method=='POST':
        if request.POST['transaction_id']:
            p.transaction_id = request.POST['transaction_id']
            p.premium = request.user
            p.save()
            return redirect('success')
        else:
            return render(request,'teacher/create.html',{'error':'Something is missing! Try again to fill the form'})
    else:
        return render(request,'teacher/payment.html')
def success(request):
    return render(request,'teacher/success.html')
@login_required
def check(request):
    teacher = Teacher.objects.get(teacher=request.user)
    creation = Create.objects
    context = {
        "teacher":teacher,
        "creation":creation,
    }

    return render(request,'teacher/check.html',context)
@login_required(login_url="/accounts/signup")
def upvote(request,teacher_id):
    if request.method == "POST":
        teacher = get_object_or_404(Teacher,pk = teacher_id)
        teacher.votes_total+=1
        teacher.save()
        return redirect('check')
@login_required(login_url="/accounts/signup")
def editform(request,teacher_id):
    if request.method=="POST":
        if request.POST['name'] and request.POST['email'] and request.POST['contact'] and request.POST['city'] and request.POST['state']:
            teacher = get_object_or_404(Teacher,pk = teacher_id)
            teacher.name = request.POST['name']
            teacher.institute_name = request.POST['institute_name']
            teacher.email = request.POST['email']
            teacher.contact = request.POST['contact']
            teacher.city = request.POST['city']
            teacher.state = request.POST['state']
            teacher.acheivements = request.POST['acheivements']
            teacher.experience = request.POST['experience']
            teacher.videolinks = request.POST['videolinks']
            teacher.image = request.FILES['image']
            teacher.class_type=request.POST['class_type']
            teacher.teacher = request.user
            teacher.save()
            return redirect('check')


        else:
            return render(request,'teacher/edit.html',{'error':'Something is missing! Try again to fill the form'})
    else:
        return render(request,'teacher/edit.html',{'k':teacher_id})
