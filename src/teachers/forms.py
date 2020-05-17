from django import forms

from teachers.models import Teacher


class TeacherCreateForm (forms.ModelForm):
    class Meta:
        model = Teacher
        fields = (
            'first_name',
            'last_name',
            'age',
            'active_groups',
            'password',
            'phone'
        )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        clened_phone = ''
        for i in phone:
            if not i.isdigit():
                raise forms.ValidationError('enter numbers only')

        return clened_phone
