from django.shortcuts import render # noqa - file not used

from django.http import HttpResponse, HttpResponseRedirect # noqa -  imported but unused

from group.models import Group # noqa -  imported but unused


def index(request):
    return render(request, 'index.html', context={})


def create_group(request):

    from group.forms import GroupCreateForm
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        form = GroupCreateForm()

    context = {'create_form': form}
    return render(request, 'create.html', context=context)
