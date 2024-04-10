from django.db import models

from entities.models import PrintPrice
from entities.models.print_order import PrintOrder


class Frame(models.Model):
    print_order = models.ForeignKey(
        PrintOrder,
        models.DO_NOTHING,
        help_text='Связь с заказом',
        db_comment='Связь с заказом'
    )
    amount = models.IntegerField(
        help_text='Количество копий',
        db_comment='Количество копий'
    )
    film_id = models.IntegerField(
        help_text='Связь с пленкой',
        db_comment='Связь с пленкой'
    )
    frame_number = models.IntegerField(
        help_text='Номер кадра'
    )
    print_price = models.ForeignKey(
        PrintPrice,
        models.DO_NOTHING,
        blank=True,
        null=True,
        help_text='Связь с ценой печати'
    )

    class Meta:
        managed = False
        db_table = 'frames'
        db_table_comment = 'Кадры'
        verbose_name = 'Кадр'
        verbose_name_plural = 'Кадры'
