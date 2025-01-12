from rest_framework import serializers

def validate_habit(data):
    if data["pleasant"] and (data.get("reward") or data.get("linked_habit")):
        raise serializers.ValidationError(
            "Приятная привычка не может иметь вознаграждение или связанную привычку."
        )
    if not data["pleasant"] and not (data.get("reward") or data.get("linked_habit")):
        raise serializers.ValidationError(
            "У полезной привычки должно быть либо вознаграждение, либо связанная привычка."
        )
    if data["duration"] > 120:
        raise serializers.ValidationError("Время выполнения не может превышать 120 секунд.")
    if data["periodicity"] > 7:
        raise serializers.ValidationError("Нельзя выполнять привычку реже, чем раз в 7 дней.")
    return data