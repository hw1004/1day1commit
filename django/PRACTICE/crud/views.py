from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def new(request):
    return render(request, 'crud/new.html')

def create(request):
    student = Student()
    student.name = request.GET['name']
    student.age = request.GET['age']
    student.major = request.GET['major']
    student.description = request.GET['description']
    student.save()
    return redirect(f'/school/{student.pk}/')

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
    return render(request, 'crud/edit.html', {
        'student': student,
    })

def update(request, pk):
    student = Student.objects.get(pk=pk)
    student.name = request.GET['name']
    student.age = request.GET['age']
    student.major = request.GET['major']
    student.description = request.GET['description']
    student.save()
    return redirect(f'/school/{student.pk}/')

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('/school/')