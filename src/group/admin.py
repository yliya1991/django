from django.contrib import admin

from group.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('id', 'first_name', 'last_name', 'group_code', 'group_number',
                    'form_of_training', 'training_completed')
    fields = ('first_name', 'last_name', 'group_code', 'group_number', 'form_of_training', 'training_completed')
    readonly_fields = ('form_of_training', 'training_completed')

<<<<<<< HEAD
=======
    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(group_code=10)

        return queryset
>>>>>>> a8aa4e4ba879bca99be5dfe897736f99e6750c8e

admin.site.register(Group, GroupAdmin) # noqa
