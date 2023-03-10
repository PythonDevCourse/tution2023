"""Модуль моделей приложения аккаунтов"""
from django.db.models.deletion import CASCADE
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
        """Имя: Текущая сумма."""
        return f"{self.name}: {self.current_sum}"


class MoneyMovement(models.Model):
    """Модель для фиксации движения денежных средств"""
    source_account = models.ForeignKey("Accounts", on_delete=CASCADE, related_name='srcacc', null=True, blank=True)
    destination_account = models.ForeignKey("Accounts", on_delete=CASCADE, related_name='dstacc')
    sum = models.IntegerField(verbose_name="Сумма в копейках")
    subject = models.CharField(verbose_name="Причина движения", max_length=128)

    def __str__(self):
        return f"{self.source_account} -> {self.destination_account} ({self.sum})"

    def save(self):
        if self.source_account is not None:
            src = self.source_account.current_sum
            self.source_account.current_sum = src - self.sum

        dst = self.destination_account.current_sum
        self.destination_account.current_sum = dst + self.sum

        if self.source_account is not None:
            self.source_account.save()

        self.destination_account.save()

        super(MoneyMovement, self).save()
