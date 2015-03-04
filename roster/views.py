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
    paginator = Paginator(course_list, 25)
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    return render(request, 'roster/course_list.html', {'courses': courses})

def studentList(request):
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 25)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    return render(request, 'roster/student_list.html', {'students': students})
