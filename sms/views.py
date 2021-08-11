from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from students.models import StudentInfo
from teachers.models import TeacherInfo


@login_required
def index(request):
    teachers = TeacherInfo.objects.all().order_by('id')
    students = StudentInfo.objects.all().order_by('id')
    paginator_teachers = Paginator(teachers, 3)
    page_teachers = request.GET.get('page')
    paged_teachers = paginator_teachers.get_page(page_teachers)
    try:
        if int(page_teachers) * 3 > teachers.count() and int(page_teachers) * 3 > teachers.count() + 1 and int(page_teachers) * 3 > teachers.count() + 2:
            paged_teachers = None
    except:
        pass
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    paged_students = paginator.get_page(page)
    context = {
        "students": paged_students,
        "teachers": paged_teachers
    }
    return render(request, "home.html", context)



