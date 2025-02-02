from django.shortcuts import render,redirect
from .models import Students
from .forms import StudentForm

# Create your views here.
def view_student(request):
    students = Students.objects.all()
    return render(request,'task2/view_student.html',{'students':students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_student')
    else:
        form = StudentForm()
    return render(request,'task2/add_student.html',{'form':form})