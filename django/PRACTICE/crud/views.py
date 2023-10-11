from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

from django.views.decorators.http import require_safe, require_http_methods, require_POST
# Create your views here.
# def new(request):
    # form = StudentForm()
    # return render(request, 'crud/new.html',{
        # 'form': form
    # })

@require_http_methods(['GET', 'POST'])
def create(request):
    # form = StudentForm(data=request.POST)
    if request.method == 'GET':
        form = StudentForm()
    
    elif request.method == 'POST':
        form = StudentForm(data=request.POST)
        
        if form.is_valid():
            student = form.save()
            return redirect('crud:detail', student.pk)

    return render(request, 'crud/form.html', {
        'form': form
    })

@require_safe
def index(request):
    students = Student.objects.all()
    return render(request, 'crud/index.html', {
        'students': students,
    })

@require_safe
def detail(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'crud/detail.html', {
        'student': student,
    })

# def edit(request, pk):
    # student = Student.objects.get(pk=pk)
    # form = StudentForm(instance=student)
    # return render(request, 'crud/edit.html', {
        # 'student': student,
        # 'form': form,
    # })
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'GET':
        form = StudentForm(instance=student)
        
    elif request.method == 'POST':
        form = StudentForm(data=request.POST, instance=student)
    
        if form.is_valid():
            student = form.save()
            return redirect('crud:detail', student.pk)

    return render(request, 'crud/form.html', {
        'form': form,
    })

@require_POST
def delete(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    # '/school/'
    return redirect('crud:index')