from django.db import models

from entities.models import Item


class ServiceTypeNeededItem(models.Model):
    item = models.OneToOneField(
        Item,
        on_delete=models.DO_NOTHING,
        primary_key=True,
        help_text='Необходимый предмет'
    )
    service_type = models.ForeignKey(
        'ServiceType',
        on_delete=models.DO_NOTHING,
        help_text='Тип услуги, к которому относится предмет'
    )
    count = models.IntegerField(
        help_text='Количество необходимых предметов'
    )

    class Meta:
        managed = False
        db_table = 'service_types_needed_items'
        unique_together = (('item', 'service_type'),)
        verbose_name = 'Необходимые предметы для типа услуги'
        verbose_name_plural = 'Необходимые предметы для типов услуг'

    def __str__(self):
        return f'{self.item} - {self.service_type}'