from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # noqa imported unused

from teachers.models import Teacher


def teachers_generate(request):
    age = request.GET.get('age')
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    teachers_filter = Teacher.objects.all()

    if age:
        teachers_filter = teachers_filter.filter(age=age)

    if first_name:
        teachers_filter = teachers_filter.filter(first_name=first_name)

    if last_name:
        teachers_filter = teachers_filter.filter(last_name=last_name)

    response = f'teachers: {teachers_filter.count()}<br/>' # noqa

    for teacher in teachers_filter:
        response += teacher.full_info() + '<br/>'

    return HttpResponse(response)


def index(request):
    return render(request, 'index.html', context={})


def create_teacher(request):
    from teachers.forms import TeacherCreateForm

    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        form = TeacherCreateForm()

    context = {'create_form': form}

    return render(request, 'create.html', context=context)
