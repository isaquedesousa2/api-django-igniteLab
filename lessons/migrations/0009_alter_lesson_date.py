# Generated by Django 4.0.5 on 2022-06-25 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0008_remove_teacher_lesson_lesson_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
