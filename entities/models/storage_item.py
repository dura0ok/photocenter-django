from django.db import models


class StorageItem(models.Model):
    storage = models.OneToOneField(
        'Storage',
        models.DO_NOTHING,
        help_text='Связь со складом зданий'
    )
    item = models.ForeignKey(
        'Item',
        models.DO_NOTHING,
        help_text='Связь с товаром'
    )
    quantity = models.IntegerField(
        help_text='Количество товаров данного типа на складе'
    )

    class Meta:
        verbose_name = 'Товар на складе'
        verbose_name_plural = 'Товары на складах'
        db_table = 'storage_items'
        constraints = [
            models.UniqueConstraint(
                fields=['storage', 'item'],
                name='storage_items_unique'
            )
        ]
        db_table_comment = 'Товары на складах зданий'

    def __str__(self):
        return f'{self.item} - {self.quantity}'
