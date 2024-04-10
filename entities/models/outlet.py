from django.db import models

from .outlet_types import OutletTypes


class Outlet(models.Model):
    type = models.ForeignKey(
        OutletTypes,
        models.DO_NOTHING,
        db_comment='Тип здания',
        help_text='Выберите тип здания.'
    )
    address = models.CharField(
        max_length=200,
        db_comment='Адрес',
        help_text='Введите адрес здания.'
    )

    class Meta:
        managed = True
        db_table = 'outlets'
        unique_together = (('type', 'address'),)
        db_table_comment = 'Здания'
        verbose_name = "Здание"
        verbose_name_plural = "Здания"

    def __str__(self):
        return f"{self.type} - {self.address}"
