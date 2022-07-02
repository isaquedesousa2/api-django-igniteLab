from .views import LessonViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('aulas', LessonViewSet)







