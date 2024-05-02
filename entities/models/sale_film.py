from django.db import models


class SaleFilm(models.Model):
    sale_order = models.ForeignKey(
        'SaleOrder',
        on_delete=models.CASCADE,
        verbose_name='Продажа пленки(подробная и',
        help_text='Ссылка на продажу товара в заказе',
        db_comment='Ссылка на продажу товара в заказе'
    )

    film_id = models.ForeignKey(
        'Film',
        on_delete=models.CASCADE,
        verbose_name='Плёнка',
        help_text='Ссылка на саму пленку',
        db_comment='Ссылка на саму пленку'
    )

    class Meta:
        db_table = 'sale_films'
        db_table_comment = 'Продажа пленок'
        verbose_name = 'Продажа пленки'
        verbose_name_plural = 'Продажи пленок'

    def __str__(self):
        return f'{self.sale_order} - {self.film_id}'
