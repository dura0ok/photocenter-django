from django.db import models

from entities.models.firm import Firm


class Item(models.Model):
    firm = models.ForeignKey(
        Firm,
        models.DO_NOTHING,
        db_comment='Связь с брэндом',
        help_text='Выберите бренд товара'
    )
    product_name = models.CharField(
        max_length=100,
        db_comment='Название товара',
        help_text='Введите название товара'
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        db_comment='Цена',
        help_text='Введите цену товара'
    )

    class Meta:
        db_table = 'items'
        unique_together = (('firm', 'product_name'),)
        db_table_comment = 'Товары'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.firm} - {self.product_name}'
