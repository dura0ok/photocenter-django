from django.db import models
from django.db.models import UniqueConstraint


class VendorItem(models.Model):
    vendor = models.ForeignKey(
        'Vendor',
        models.DO_NOTHING,
        db_comment='Связь с поставщиком'
    )
    item = models.ForeignKey(
        'Item',
        models.DO_NOTHING,
        db_comment='Связь с товаром'
    )
    current_price = models.IntegerField(
        blank=True,
        null=True,
        db_comment='Текущая цена по которой продает поставщик данный товар'
    )

    class Meta:
        db_table = 'vendor_items'
        constraints = [
            models.UniqueConstraint(
                fields=['vendor', 'item'],
                name='vendor_items_unique'
            )
        ]

        verbose_name = 'Товар поставщика'
        verbose_name_plural = 'Товары поставщика'
        db_table_comment = 'По какой цене продает поставщик товары'

    def __str__(self):
        return f'{self.vendor} - ({self.item})'
