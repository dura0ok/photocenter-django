from django.db import models
from django.db.models import UniqueConstraint

from entities.models import Vendor, Item


class VendorItem(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        models.DO_NOTHING,
        db_comment='Связь с поставщиком',
        help_text='Выберите поставщика товара'
    )
    item = models.ForeignKey(
        Item,
        models.DO_NOTHING,
        db_comment='Связь с товаром',
        help_text='Выберите товар'
    )
    current_price = models.IntegerField(
        blank=True,
        null=True,
        db_comment='Текущая цена по которой продает поставщик данный товар',
        help_text='Введите текущую цену по которой продает поставщик данный товар'
    )

    class Meta:
        db_table = 'vendor_items'
        db_table_comment = 'По какой цене продает поставщик товары'
        verbose_name = 'Товар поставщика'
        verbose_name_plural = 'Товары поставщиков'
        constraints = [
            UniqueConstraint(fields=['vendor', 'item'], name='unique_vendor_item')
        ]

    def __str__(self):
        return f'{self.vendor} - ({self.item})'
