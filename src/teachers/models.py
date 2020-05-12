from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()
    specification = models.CharField(max_length=32)
    active_groups = models.PositiveSmallIntegerField()
    password = models.CharField(max_length=120, default='')

    @property
    def info(self):
        return f'{self.id}. {self.first_name} {self.last_name} {self.age} {self.specification}' # noqa

    def full_info(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.age} {self.specification} {self.active_groups}'
