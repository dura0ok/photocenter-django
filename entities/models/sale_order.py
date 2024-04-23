from django.db import models

from entities.models import Order, Item


class SaleOrder(models.Model):
    order = models.ForeignKey(
        Order,
        models.DO_NOTHING,
        blank=True,
        null=True,
        help_text='Связь с заказом',
        db_comment='Связь с заказом'
    )
    item = models.ForeignKey(
        Item,
        models.DO_NOTHING,
        help_text='Связь с товарами',
        db_comment='Связь с товарами'
    )
    amount = models.IntegerField(
        help_text='Количество',
        db_comment='Количество'
    )

    class Meta:
        db_table = 'sale_orders'
        db_table_comment = 'Продажи товаров в заказе'
        verbose_name = 'Продажа товара в заказе'
        verbose_name_plural = 'Продажи товаров в заказе'

    def __str__(self):
        return f'{self.order} {self.item} {self.amount}'
