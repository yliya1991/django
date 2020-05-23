from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()
    specification = models.CharField(max_length=32)
    active_groups = models.PositiveSmallIntegerField()
    password = models.CharField(max_length=120, default='')
    phone = models.CharField(max_length=24, default='')

    @property
    def info(self):
        return f'{self.id}. {self.first_name} {self.last_name} {self.age} {self.specification}' # noqa

    def full_info(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.age} {self.specification} {self.active_groups}'

    def info_teachers(self):
<<<<<<< HEAD
        return f'{self.first_name} {self.last_name} {self.age} {self.specification}' # noqa'


class Logger(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=64)
    execution_time = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
=======
        return f'{self.first_name} {self.last_name} {self.age} {self.specification}' # noqa'
>>>>>>> a8aa4e4ba879bca99be5dfe897736f99e6750c8e
