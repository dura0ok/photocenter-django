from django.db import models


class Firm(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text='Введите название бренда.',
        db_comment='Название Бренда'
    )

    class Meta:
        managed = False
        db_table = 'firms'
        db_table_comment = 'Бренды товаров'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return f'{self.name}'
