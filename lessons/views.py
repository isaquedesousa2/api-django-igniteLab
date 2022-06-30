from rest_framework import viewsets
from rest_framework.response import Response
from .models import Lesson
from .serializers import LessonSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        slug = self.request.query_params.get('slug', '')

        if slug != '':
            qs = qs.filter(slug=slug)

        return qs
    