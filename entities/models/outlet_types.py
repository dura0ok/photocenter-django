from django.db import models


class OutletTypes(models.Model):
    name = models.CharField(
        unique=True,
        max_length=200,
        help_text='Введите название типа здания.'
    )

    class Meta:
        db_table = 'outlet_types'
        db_table_comment = 'Типы зданий'
        verbose_name = 'Тип здания'
        verbose_name_plural = 'Типы зданий'

    def __str__(self):
        return self.name
