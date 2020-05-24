import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0007_logger'),
        ('students', '0001_initial'),
        ('group', '0002_auto_20200517_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='curator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='head',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Student'),
        ),
    ]
