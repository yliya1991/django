import random

from django.http import HttpResponse
from django.shortcuts import render  # noqa -  imported but unused

from faker import Faker

from students.models import Student


def index(request):

    return render(request, 'index.html')


def generate_student(request):
    fake = Faker()
    student = Student.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=(random.randrange(12, 60, 1)))
    response = f'student ID {student.info( )} age<br/>' # noqa

    return HttpResponse(response)


def std_generate(count: int = 1) -> str:
    fake = Faker()
    all_response = ''

    for _ in range(int(count)):
        student = Student.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=(random.randrange(12, 60, 1)))

        response = f'student ID {student.info()} age<br/>'
        all_response += response

    return HttpResponse(all_response)


def generate_students(request):
    std_count = request.GET['count']
    if std_count.isdigit() and 1 <= int(std_count) <= 100:

        return HttpResponse(std_generate(int(request.GET['count'])))
    else:
        return HttpResponse(
            f'value should be less than 101 but not less than -1'
        )
