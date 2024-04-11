from django.db import models


class Frame(models.Model):
    print_order = models.ForeignKey(
        'PrintOrder',
        models.DO_NOTHING,
        help_text='Связь с заказом',
        db_comment='Связь с заказом'
    )
    amount = models.IntegerField(
        help_text='Количество копий',
        db_comment='Количество копий'
    )
    film = models.ForeignKey(
        'Film',
        models.DO_NOTHING,
        db_comment='Связь с пленкой',
        help_text='Кадр на какой пленке?'
    )

    frame_number = models.IntegerField(
        help_text='Номер кадра'
    )
    print_price = models.ForeignKey(
        'PrintPrice',
        models.DO_NOTHING,
        blank=True,
        null=True,
        help_text='Связь с ценой печати'
    )

    class Meta:
        db_table = 'frames'
        db_table_comment = 'Кадры'
        verbose_name = 'Кадр'
        verbose_name_plural = 'Кадры'

    def __str__(self):
        return f'{self.print_order} - {self.film}'
