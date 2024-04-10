from django.db import models

from entities.models import Order


class ServiceOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.DO_NOTHING,
        db_comment='Связь с заказом',
        help_text='Связь с заказом'
    )
    service_type = models.OneToOneField(
        'ServiceTypeOutlet',
        on_delete=models.DO_NOTHING,
        primary_key=True,
        db_comment='Связь с типом услуги',
        help_text='Связь с типом услуги'
    )
    count = models.IntegerField(
        db_comment='Количество таких услуг заказанных',
        help_text='Количество таких услуг заказанных'
    )

    class Meta:
        managed = False
        db_table = 'service_orders'
        unique_together = (('service_type', 'order'),)
        db_table_comment = 'Заказ услуг'
        verbose_name = 'Заказ услуги'
        verbose_name_plural = 'Заказы услуг'

    def __str__(self):
        return f'{self.order} {self.service_type}'
