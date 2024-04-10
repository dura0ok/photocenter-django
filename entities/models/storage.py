from django.db import models


class Storage(models.Model):
    is_main_storage = models.BooleanField(
        blank=True,
        null=True,
        help_text='Связь с главным складом'
    )
    capacity = models.IntegerField(
        help_text='Вместимость'
    )
    outlet = models.ForeignKey(
        'Outlet',
        models.DO_NOTHING,
        help_text='Связь со зданием'
    )

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        managed = False
        db_table = 'storage'
        db_table_comment = 'Склады зданий'

    def __str__(self):
        return f"{self.outlet}"