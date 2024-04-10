from django.db import models


class PrintPrice(models.Model):
    paper_size = models.ForeignKey(
        'PaperSize',
        models.DO_NOTHING,
        help_text='Выберите формат бумаги',
        db_comment='Формат бумаги'
    )
    paper_type = models.ForeignKey(
        'PaperType',
        models.DO_NOTHING,
        help_text='Выберите тип бумаги',
        db_comment='Тип бумаги'
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        help_text='Укажите цену за (формат, печать)',
        db_comment='Цена за (формат, печать)'
    )

    class Meta:
        managed = False
        db_table = 'print_prices'
        unique_together = (('paper_size', 'paper_type'),)
        db_table_comment = 'Расценки на печать'
        verbose_name = 'Расценка на печать'
        verbose_name_plural = 'Расценки на печать'

    def __str__(self):
        return f'{self.paper_type.name} - {self.paper_size}'
