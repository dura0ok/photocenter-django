from django.db import models


class Frame(models.Model):
    print_order = models.ForeignKey(
        'PrintOrder',
        on_delete=models.CASCADE,
        verbose_name='Заказ',
        help_text='Связь с частью заказа на печать',
        db_comment='Связь с заказом'
    )

    amount = models.IntegerField(
        verbose_name='Копии',
        help_text='Количество копий',
        db_comment='Количество копий'
    )

    film = models.ForeignKey(
        'Film',
        on_delete=models.CASCADE,
        verbose_name='Плёнка',
        db_comment='Связь с пленкой',
        help_text='Кадр на какой пленке?'
    )

    frame_number = models.IntegerField(
        verbose_name='Кадр',
        help_text='Номер кадра'
    )

    print_price = models.ForeignKey(
        'PrintPrice',
        on_delete=models.CASCADE,
        verbose_name='Цена',
        help_text='Связь с ценой печати'
    )

    class Meta:
        db_table = 'frames'
        db_table_comment = 'Кадры'
        verbose_name = 'Кадр'
        verbose_name_plural = 'Кадры'

    def __str__(self):
        return f'{self.print_order} - {self.film}'
