from django.shortcuts import render , redirect
from .models import StudentModel
from .forms import StudentForm

def add_student(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("display_student")
        
        else:
            form=StudentForm()
            return render(request,"add_student.html",{'form':form})
        
    else:
        form=StudentForm()
        return render(request,"add_student.html",{'form':form})

def display_student(request):
    stu=StudentModel.objects.all()
    return render(request,"display_student.html",{'stu':stu})

def delete_student(request,id):
    obj=StudentModel.objects.get(pk=id)
    obj.delete()
    return redirect("display_student")

def update_student(request,id):
    obj=StudentModel.objects.get(id=id)
    form=StudentForm(instance=obj)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("display_student")
        
        else:
            form=StudentForm()
            return render(request,"update_student.html",{'form':form})
    
    else:
        form=StudentForm()
        return render(request,"update_student.html",{'form':form})
        