from django.db import models
from django.db.models import UniqueConstraint

from entities.models import Item
from entities.models.delivery import Delivery


class DeliveryItem(models.Model):
    delivery = models.OneToOneField(
        Delivery,
        models.DO_NOTHING,
        help_text='Поставка'
    )

    item = models.ForeignKey(
        Item,
        models.DO_NOTHING,
        help_text='Товар'
    )

    purchase_price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        help_text='Цена закупки товара'
    )

    amount = models.IntegerField(
        help_text='Количество поставленных единиц товара'
    )

    class Meta:
        db_table = 'delivery_items'
        # constraints = [
        #     UniqueConstraint(
        #         fields=['delivery', 'item'],
        #         name='delivery_items_unique')
        # ]
        verbose_name = 'Товар в поставке'
        verbose_name_plural = 'Товары в поставке'
        db_table_comment = 'Товары в поставке'

    def __str__(self):
        return f'{self.delivery} - {self.item}'
