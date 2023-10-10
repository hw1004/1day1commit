from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# Create your views here.
def new(request):
    form = StudentForm()
    return render(request, 'crud/new.html',{
        'form': form
    })

def create(request):
    form = StudentForm(data=request.POST)
    
    if form.is_valid():
        student = form.save()
        return redirect('crud:detail', student.pk)
    else:
        return render(request, 'board:detail', {
            'form': form
        })

def index(request):
    students = Student.objects.all()
    return render(request, 'crud/index.html', {
        'students': students,
    })

def detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'crud/detail.html', {
        'student': student,
    })

def edit(request, pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)
    return render(request, 'crud/edit.html', {
        'student': student,
        'form': form,
    })

def update(request, pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(data=request.POST, instance=student)
    
    if form.is_valid():
        student = form.save()
        return redirect('crud:detail', student.pk)
    else:
        return render(request, 'crud/edit.html', {
            'student': student,
            'form': form
        })

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    # '/school/'
    return redirect('crud:index')