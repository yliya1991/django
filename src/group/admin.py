from django.contrib import admin

from group.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('id', 'first_name', 'last_name', 'group_code', 'group_number',
                    'form_of_training', 'training_completed')
    fields = ('first_name', 'last_name', 'group_code', 'group_number', 'form_of_training', 'training_completed')
    readonly_fields = ('form_of_training', 'training_completed')


admin.site.register(Group, GroupAdmin) # noqa
