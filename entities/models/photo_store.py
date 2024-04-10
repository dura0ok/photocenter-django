from django.db import models

from entities.models import Outlet


class PhotoStore(models.Model):
    outlet = models.OneToOneField(
        Outlet,
        models.DO_NOTHING,
        primary_key=True,
        db_comment='Привязка к зданию',
        help_text='Связь со зданием в котором расположен фотомагазин'
    )

    num_workers = models.IntegerField(
        help_text='Количество работников в фотомагазине'
    )

    class Meta:
        db_table = 'photo_stores'
        db_table_comment = 'Фотомагазины'
        verbose_name = 'Фотомагазин'
        verbose_name_plural = 'Фотомагазины'

    def __str__(self):
        return f'{self.outlet.address}'
