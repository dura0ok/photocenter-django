from django.db import models


class Order(models.Model):
    client = models.ForeignKey(
        'Client',
        models.DO_NOTHING,
        help_text='Клиент, который сделал заказ',
        db_comment='Клиент, который сделал заказ'
    )
    accept_outlet = models.ForeignKey(
        'Outlet',
        models.DO_NOTHING,
        help_text='Где приняли заказ',
        db_comment='Где приняли заказ'
    )
    accept_timestamp = models.DateTimeField(
        help_text='Когда заказ поступил',
        db_comment='Когда заказ поступил'
    )
    total_amount_price = models.IntegerField(
        help_text='Суммарная цена заказа, которая рассчитывается из купленных товаров, услуг....',
        db_comment='Суммарная цена заказа, которая рассчитывается из купленных товаров, услуг....'
    )
    is_urgent = models.BooleanField(
        help_text='Срочность заказа',
        db_comment='Срочность заказа'
    )

    class Meta:
        managed = False
        db_table = 'orders'
        db_table_comment = 'Заказы'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.client} - {self.accept_timestamp}'
