from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from .models import Task

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer