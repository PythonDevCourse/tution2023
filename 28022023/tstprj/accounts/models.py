"""Модуль моделей приложения аккаунтов"""
from datetime import datetime

from django.db import models


class Accounts(models.Model):
    """Модель аккаунтов (мест где храняться денежные средства)."""

    name = models.CharField(max_length=128)
    current_sum = models.IntegerField()  # сумма счета в копейках
    starting_sum = models.IntegerField()
    creation_date = models.DateTimeField()
    modification_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        """Имя: Текузая сумма."""
        return f"{self.name}: {self.current_sum}"
