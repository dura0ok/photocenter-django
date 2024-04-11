from django.db import models


class FilmDevelopmentOrder(models.Model):
    code = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        help_text='Уникальный код пленки',
        db_comment='Уникальный код пленки'
    )
    order = models.ForeignKey(
        'Order',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        help_text='Связь с заказом',
        db_comment='Связь с заказом'
    )

    class Meta:
        db_table = 'film_development_orders'
        db_table_comment = 'Проявка пленок(вложено в чек заказа)'
        verbose_name = 'Проявка пленок'
        verbose_name_plural = 'Проявка пленок'

    def __str__(self):
        return f'{self.order} - {self.code}'
