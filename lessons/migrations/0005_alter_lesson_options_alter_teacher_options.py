# Generated by Django 4.0.5 on 2022-06-24 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_remove_lesson_teacher_name_lesson_teacher_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Aula', 'verbose_name_plural': 'Aulas'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Professor(a)', 'verbose_name_plural': 'Professores(a)'},
        ),
    ]
