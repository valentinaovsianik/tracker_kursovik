from datetime import timedelta

from django.db import models

from users.models import User


class Habit(models.Model):
    """Модель привычки"""

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_habits",
        verbose_name="Создатель привычкм",
        help_text="Пользователь, который создал эту привычку.",
    )
    action = models.CharField(
        max_length=255,
        verbose_name="Действие",
        help_text="Действие, которое вы хотите превратить в привычку (например, 'Медитировать').",
    )
    time = models.TimeField(
        verbose_name="Время", help_text="Выберите время суток, когда вы собираетесь выполнять привычку."
    )
    place = models.CharField(
        max_length=255, verbose_name="Место", help_text="Место выполнения привычки (например, 'Дома' или 'Спортзал')."
    )
    pleasant = models.BooleanField(
        default=False,
        verbose_name="Приятная привычка",
        help_text="Является ли привычка приятной? Установите True, если да.",
    )
    linked_habit = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        help_text="Связанная привычка, которая выполняется вместе с этой (необязательно).",
    )
    reward = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Вознаграждение после выполнения привычки",
        help_text="Вознаграждение, которое вы получите за выполнение привычки (необязательно).",
    )
    duration = models.PositiveIntegerField(
        default=timedelta(seconds=120),
        verbose_name="Продолжительность",
        help_text="Продолжительность выполнения привычки в секундах (максимум 120 секунд).",
    )
    periodicity = models.PositiveIntegerField(
        default=1,
        verbose_name="Периодичность",
        help_text="Как часто привычка должна выполняться (в днях, максимум раз в 7 дней).",
    )
    public = models.BooleanField(
        default=False,
        verbose_name="Публичная привычка",
        help_text="Доступна ли привычка для просмотра другими пользователями?",
    )

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.pleasant and (self.reward or self.linked_habit):
            raise ValidationError("Приятная привычка не может иметь вознаграждение или связанную привычку.")
        if not self.pleasant and not (self.reward or self.linked_habit):
            raise ValidationError("У полезной привычки должно быть либо вознаграждение, либо связанная привычка.")
        if self.duration > 120:
            raise ValidationError("Время выполнения не может превышать 120 секунд.")
        if self.periodicity > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем раз в 7 дней.")

    def __str__(self):
        return f"{self.action} ({self.creator.username})"
