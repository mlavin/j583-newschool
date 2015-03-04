# roster/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from roster.models import Course, Student

def home(request):
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
    }
    return render(request, 'roster/home.html', context)

def course(request, pk):
    course = get_object_or_404(Course, id=pk)
    return render(request, 'roster/course.html', {'course': course})

def student(request, pk):
    student = get_object_or_404(Student, id=pk)
    return render(request, 'roster/student.html', {'student': student})

def courseList(request):
    course_list = Course.objects.all()
    return render(request, 'roster/course_list.html', {'courses': course_list})

def studentList(request):
    student_list = Student.objects.all()
    return render(request, 'roster/student_list.html', {'students': student_list})
