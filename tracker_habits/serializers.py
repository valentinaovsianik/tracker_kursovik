from rest_framework import serializers
from .models import Habit
from .validators import validate_habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        return validate_habit(data)
