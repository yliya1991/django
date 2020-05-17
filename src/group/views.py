from django.shortcuts import get_object_or_404, redirect, render, reverse

from django.http import HttpResponse, HttpResponseRedirect # noqa -  imported but unused

from group.forms import GroupCreateForm
from group.models import Group # noqa -  imported but unused


def show_group(request):
    group = Group.objects.all()
    count = group.count()

    return render(request, 'group-list.html', context={'group': group, 'count': count})


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


def edit_group(request, pk):
    group = get_object_or_404(Group, id=pk)

    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect(reverse('group:list'))
    elif request.method == 'GET':
        form = GroupCreateForm(instance=group)

    context = {'edit_form': form,
               'group': group,
               }

    return render(request, 'edit-group.html', context=context)


def delete_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    group.delete()
    return redirect(reverse('group:list'))
