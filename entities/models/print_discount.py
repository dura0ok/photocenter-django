from django.db import models


class PrintDiscount(models.Model):
    photo_amount = models.IntegerField(
        unique=True,
        help_text='Количество фотографий, критерий',
        db_comment='Количество фотографий, критерий'
    )
    discount = models.IntegerField(
        help_text='Размер скидки в процентах',
        db_comment='Размер скидки в процентах'
    )

    class Meta:
        db_table = 'print_discounts'
        db_table_comment = 'Скидка на печать'
        verbose_name = 'Скидка на печать'
        verbose_name_plural = 'Скидки на печать'

    def __str__(self):
        return f"Количество {self.photo_amount} - Скидка {self.photo_amount}%"
