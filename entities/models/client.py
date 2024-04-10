from django.db import models


class Client(models.Model):
    full_name = models.CharField(
        max_length=50,
        db_comment='ФИО клиента',
        help_text='Введите ФИО клиента.'
    )
    is_professional = models.BooleanField(
        db_comment='Профессионал или Любитель?',
        help_text='Отметьте, если клиент является профессионалом.'
    )
    discount = models.IntegerField(
        db_comment='Персональная скидка',
        help_text='Введите персональную скидку клиента.'
    )
    discount_card = models.BooleanField(
        blank=True,
        null=True,
        help_text='Отметьте, если у клиента есть дисконтная карта.'
    )

    class Meta:
        verbose_name = 'Клиент(а)'
        verbose_name_plural = 'Клиенты'
        db_table = 'clients'
        db_table_comment = 'Таблица клиентов различных фотоцентров'

    def __str__(self):
        return self.full_name

