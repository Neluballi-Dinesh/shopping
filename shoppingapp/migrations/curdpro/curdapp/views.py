from django.shortcuts import render,redirect

from .models import StudentsData
def mainPage(request):
    students=StudentsData.objects.all()
    return render(request,'mainPage.html',{'students':students})

def add_student(request):
    if request.method=='GET':
        return render(request,'add_student.html')
    else:
        StudentsData(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        course=request.POST['course'],
        fee=request.POST['fee'],
        iname=request.POST['iname'],
        location=request.POST['location']
        ).save()
        return redirect('mainPage')


def update(request,id):
    if request.method=='GET':
        student=StudentsData.objects.get(id=id)
        return render(request,'update.html',{'student':student})
    else:
        student=StudentsData.objects.get(id=id)
        student.first_name=request.POST['fname']
        student.last_name=request.POST['lname']
        student.email=request.POST['email']
        student.mobile=request.POST['mobile']
        student.course=request.POST['course']
        student.fee=request.POST['fee']
        student.iname=request.POST['iname']
        student.location=request.POST['location']
        save()
        return redirect('mainPage')


def delete(request,id):
    student=StudentsData.objects.get(id=id)
    student.delete()
    return redirect('mainPage')
