import random

from django.core.management.base import BaseCommand # noqa imported but unused

from faker import Faker

from teachers.models import Teacher


class Commands(BaseCommand):
    help = 'Generate new random teachers' # noqa is a python builtin

    def add_arguments(self, parser):
        parser.add_argument('value', nargs='?', type=int, help='Value teachers', default=100)

    def handle(self, *args, **options):
        value = options['value']
        fake = Faker()
        group_random = random.randint(1, 5)
        for _ in range(value):
            Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(20, 60),
                specification=fake.first_name(),
                active_groups=group_random,
            )


class Command(BaseCommand):
    help = 'Generate random teacher' # noqa

    def handle(self, *args, **options):
        fake = Faker()

        teachers = []
        for _ in range(1000):
            teachers.append(Teacher(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(10, 100),
            ))
        Teacher.objects.bulk_create(teachers)
