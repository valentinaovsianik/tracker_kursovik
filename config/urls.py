from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

# Временное представление для теста
def home_view(request):
    return HttpResponse("Welcome to the Home Page!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("tracker_habits/", include("tracker_habits.urls", namespace="tracker_habits")),
    path("", home_view, name="home"),  # Добавлен маршрут для корневого пути
]
