from django.shortcuts import get_object_or_404, redirect, render, reverse

<<<<<<< HEAD
from teachers.forms import ContactUsForm, TeacherCreateForm
=======
from teachers.forms import TeacherCreateForm
>>>>>>> a8aa4e4ba879bca99be5dfe897736f99e6750c8e
from teachers.models import Teacher
from teachers.tasks import send_lmail


def show_teachers(request):

    params = ['first_name',
              'last_name',
              'age',
              'age__gt',
              'age__lt',
              'age__lte',
              'age__gte',
              'specification',
              'active_groups'
              ]

    teachers = Teacher.objects.all()

    for param in params:
        value = request.GET.get(param)
        if value:
            teachers = teachers.filter(**{param: value})

    count = teachers.count()
    return render(request, 'teachers-list.html', context={'teachers': teachers,
                                                          'count': count})


def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('teachers:list'))
    elif request.method == 'GET':
        form = TeacherCreateForm()

    context = {'form_name': 'CREATE TEACHER',
               'create_form': form}
    return render(request, 'create.html', context=context)


def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)

    if request.method == 'POST':
        form = TeacherCreateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect(reverse('teachers:list'))
    elif request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)

    context = {'edit_form': form,
               'teacher': teacher,
               }

    return render(request, 'edit-teacher.html', context=context)


<<<<<<< HEAD
def index(request):
    return render(request, 'index.html')


=======
>>>>>>> a8aa4e4ba879bca99be5dfe897736f99e6750c8e
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    teacher.delete()
    return redirect(reverse('teachers:list'))
<<<<<<< HEAD


def email(request):
    if request.method == 'POST':
        email_form = ContactUsForm(request.POST)

        if email_form.is_valid():
            send_lmail.delay(request.POST)
            return redirect(reverse('index'))
            ContactUsForm.save()
            email.success(request, 'Message sent successfully')
            return redirect('email:email')
        else:
            email.error(request, 'Error sending your Message')

    elif request.method == 'GET':
        email_form = ContactUsForm()
    return render(request, 'email_form.html', context={'email_form': email_form})
=======
>>>>>>> a8aa4e4ba879bca99be5dfe897736f99e6750c8e
