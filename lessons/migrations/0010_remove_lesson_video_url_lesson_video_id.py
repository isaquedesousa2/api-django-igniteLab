# Generated by Django 4.0.5 on 2022-06-26 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0009_alter_lesson_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='video_url',
        ),
        migrations.AddField(
            model_name='lesson',
            name='video_id',
            field=models.CharField(default=1, max_length=255, verbose_name='Video ID'),
            preserve_default=False,
        ),
    ]
