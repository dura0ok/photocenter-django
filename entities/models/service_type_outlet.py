from django.db import models

from entities.models import OutletType, ServiceType


class ServiceTypeOutlet(models.Model):
    service_type = models.ForeignKey(
        ServiceType,
        on_delete=models.DO_NOTHING,
        help_text='Тип услуги'
    )
    outlet_type = models.ForeignKey(
        OutletType,
        on_delete=models.DO_NOTHING,
        help_text='Тип точки обслуживания'
    )

    class Meta:
        managed = False
        db_table = 'service_types_outlets'
        db_table_comment = 'Типы услуг'
        verbose_name = 'Вид услуги в точке обслуживания'
        verbose_name_plural = 'Виды услуг в точках обслуживания'

    def __str__(self):
        return f"{self.service_type} - {self.outlet_type}"
