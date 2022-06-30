from django.contrib import admin
from django.urls import path, include
from lessons.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]