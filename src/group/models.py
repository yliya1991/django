from django.db import models


class Group(models.Model):
    group_code = models.PositiveIntegerField()
    group_number = models.PositiveIntegerField()
    form_of_training = models.CharField(max_length=64)
    training_completed = models.BooleanField()
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    @property
    def full_group(self):
        return f'{self.group_code} {self.group_number} {self.form_of_training} {self.training_completed} {self.first_name} {self.last_name}' # noqa - E501 line too long (140 > 120 characters)

    def info(self):
        return f'{self.group_code} {self.group_number}' \
               f' {self.form_of_training}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
