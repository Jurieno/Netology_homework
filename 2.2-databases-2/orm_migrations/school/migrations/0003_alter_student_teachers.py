# Generated by Django 4.2.3 on 2023-07-25 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_student_teacher_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='teachers', to='school.teacher', verbose_name='Учителя'),
        ),
    ]
