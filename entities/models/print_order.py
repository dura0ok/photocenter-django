from django.db import models


class PrintOrder(models.Model):
    order = models.ForeignKey(
        'Order',
        models.DO_NOTHING,
        help_text='Связь с заказом',
        db_comment='Связь с заказом'
    )
    discount = models.ForeignKey(
        'PrintDiscount',
        models.DO_NOTHING,
        blank=True,
        null=True,
        help_text='Скидка',
        db_comment='Скидка'
    )

    class Meta:
        managed = False
        db_table = 'print_orders'
        db_table_comment = 'Заказы на печать'
        verbose_name = 'Заказ на печать'
        verbose_name_plural = 'Заказы на печать'

    def __str__(self):
        return f'{self.order} - {self.discount}'
