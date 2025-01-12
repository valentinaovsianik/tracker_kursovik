from django.contrib import admin
from tracker_habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "creator",
        "action",
        "time",
        "place",
        "pleasant",
        "linked_habit",
        "reward",
        "duration",
        "periodicity",
        "public",
    )
    search_fields = ("action", "place", "reward")
    list_filter = ("pleasant", "public", "periodicity")
