from django.shortcuts import render,redirect
from django.http import HttpResponse
from cmsapp.models import Department,User,Teacher,Student
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def index(request):
    return render(request,"index.html")


def dep_add(request):
    if request.method=="POST":
        d=request.POST["dep"]
        x=Department.objects.create(Dep_Name=d)
        x.save()
        return HttpResponse("success")
    else:
        return render(request,"dep_add.html")
    

def adminhome(request):
    return render(request,"adminhome.html")

def mainhome(request):
    return render(request,"mainhome.html")

def  reg_teacher(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        q=request.POST['qual']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype='teacher')
        x.save()
        y=Teacher.objects.create(tid=x,depid_id=d,Age=a,Address=ad,Qualification=q)
        y.save()
        # return HttpResponse(<scrip)
        return render(request,'adminhome.html')
    else:
        x=Department.objects.all()
        return render(request,'reg_teacher.html',{'x1':x})



def  reg_student(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype='student',is_active=False)
        x.save()
        y=Student.objects.create(depid_id=d,sid=x,Age=a,Address=ad)
        y.save()
        return HttpResponse("<script>window.alert('sstudent Registred');window.location.href='+'</script>" )
    
        # return render(request,'reg_student.html')
    else:
        x=Department.objects.all()
        return render(request,'reg_student.html',{'x1':x})

def viewstudent(request):
    x=Student.objects.all()
    return render(request,'viewstudent.html',{'x1':x})

def approve(request,aid):
    st=Student.objects.get(id=aid)
    st.sid.is_active=True
    st.sid.save()
    return redirect(viewstudent)


def teacherhome(request):
    return render(request,"teacherhome.html")
def studenthome(request):
    return render(request,"studenthome.html")


def logins(request):
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        User=authenticate(request,username=u,password=p)
        if User is not None and User.is_superuser==1:
            return redirect(adminhome)
        elif User is not None and User.usertype=="teacher":
            login(request,User)
            request.session['tech_id']=User.id
            return redirect(teacherhome)
        elif User is not None and User.usertype=='student' and User.is_active==1:
            login(request,User)
            request.session['stu_id']=User.id
            return redirect(studenthome)
        else:
            return HttpResponse("not vaild")
    else:
        return render(request,'logins.html')
    
def lgout(request):
    logout(request)
    return redirect(mainhome)

    
def approved_therview(request):
    x=User.objects.filter(is_active=1,usertype="teacher")
    return render(request,'approved_therview.html',{'xt':x})

def approved_stview(request):
    x=User.objects.filter(is_active=1,usertype="student")
    return render(request,'approved_stview.html',{'xs':x})

def updatest(request):
    stud=request.session.get('stu_id')
    student=Student.objects.get(sid_id=stud)
    user=User.objects.get(id=stud)
    return render(request,'updatest.html',{'view':student,'data':user})

def updatestudent(request,uid):
    if request.method=='POST':
        stud=Student.objects.get(id=uid)
        sid=stud.sid_id
        user=User.objects.get(id=sid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        stud.Age=request.POST['age']
        stud.Address=request.POST['address']
        stud.save()
        return HttpResponse("<script>window.alert('Update success ');window.location.href='/studenthome'</script>" )
        # return HttpResponse("success")


def updatether(request):
    teac=request.session.get('tech_id')
    teacher=Teacher.objects.get(tid__id=teac)
    tuser=User.objects.get(id=teac)
    return render(request,'updatete.html',{'tview':teacher,'tdata':tuser})

def updatetecher(request,teid):
    if request.method=='POST':
        teac=Teacher.objects.get(id=teid)
        tid=teac.tid_id
        tuser=User.objects.get(id=tid)
        tuser.first_name=request.POST['fname']
        tuser.last_name=request.POST['lname']
        tuser.email=request.POST['email']
        tuser.username=request.POST['uname']
        tuser.save()
        teac.Age=request.POST['age']
        teac.Address=request.POST['address']
        teac.save()
        return HttpResponse('success')
        
        

def deletest(request,sid):
    x=User.objects.get(id=sid)
    x.delete()
    return  HttpResponse("done")

def deletete(request,tid):
    x=User.objects.get(id=tid)
    x.delete()
    return  HttpResponse("done")


def test(request):
    return render(request,"1test.html")