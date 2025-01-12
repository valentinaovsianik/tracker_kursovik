from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import HabitViewSet, PublicHabitList

router = SimpleRouter()
router.register(r"habits", HabitViewSet, basename="habits")

app_name = "tracker_habits"

urlpatterns = [
    path("public-habits/", PublicHabitList.as_view(), name="public-habits"),
]

urlpatterns += router.urls
