from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,task_statistics

router = DefaultRouter()
router.register(r'Task_Update', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('statistics/', task_statistics),
]
