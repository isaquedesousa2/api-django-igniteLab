from asyncore import read
from rest_framework import serializers
from .models import Lesson, Teacher

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = (
            'teacher',
            'image_url'
        )

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = [
            'id',
            'title',
            'description',
            'date',
            'slug',
            #'video_id',
            'lesson_type',
            'teacher'
        ]
    
    teacher = TeacherSerializer()
