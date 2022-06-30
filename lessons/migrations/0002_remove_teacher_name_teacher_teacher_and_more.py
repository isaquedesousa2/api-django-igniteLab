# Generated by Django 4.0.5 on 2022-06-24 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='name',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='Professor(a)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data da criação'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(choices=[('AO VIVO', 'AO VIVO'), ('AULA PRÁTICA', 'AULA PRÁTICA')], max_length=20, verbose_name='Tipo da aula'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oi', to='lessons.teacher', verbose_name='Professor(a)'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='Data da atualizção'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video_url',
            field=models.CharField(max_length=255, verbose_name='Video Url'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data da criação'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='Data da atualizção'),
        ),
    ]