from django.db import models

from entities.models import Vendor, Storage


class Delivery(models.Model):
    storage = models.ForeignKey(Storage, models.DO_NOTHING, help_text='Связь с главным складом')
    vendor = models.ForeignKey(Vendor, models.DO_NOTHING, help_text='Связь с поставщиком')
    delivery_date = models.DateField(help_text='Дата поставки')

    class Meta:
        db_table = 'deliveries'
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'
        db_table_comment = 'Поставки в главный склад'

    def __str__(self):
        return f'{self.storage} {self.vendor} {self.delivery_date}'
