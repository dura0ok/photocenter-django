from django.db import models

from entities.models import Branch


class Kiosk(models.Model):
    outlet = models.OneToOneField(
        'Outlet',
        models.DO_NOTHING,
        primary_key=True,
        db_comment='Здание где расположен',
        help_text='Связь со зданием в котором расположен киоск',
    )
    branch_outlet = models.ForeignKey(
        Branch,
        models.DO_NOTHING,
        db_comment='Киоск связан с филиаом',
        help_text='Связь с филиалом, к которому прикреплен киоск'
    )

    class Meta:
        db_table = 'kiosks'
        db_table_comment = 'Киоск'
        verbose_name = 'Киоск'
        verbose_name_plural = 'Киоски'

    def __str__(self):
        return f'{self.outlet.address}'
