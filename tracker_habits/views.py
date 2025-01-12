from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView

from .models import Habit
from .serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """CRUD модели привычка"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class PublicHabitList(ListAPIView):
    """Список публичных привычек"""
    queryset = Habit.objects.filter(public=True)
    serializer_class = HabitSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # Пример возвращаемого ответа
        return Response({"public_habits": []})
