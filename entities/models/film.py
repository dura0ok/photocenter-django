from django.db import models


class Film(models.Model):
    code = models.CharField(
        verbose_name='Код',
        help_text='Уникальный код фотопленки',
        unique=True,
        max_length=255,
    )

    class Meta:
        db_table = 'films'
        verbose_name = 'Фотопленка'
        verbose_name_plural = 'Фотопленки'

    def __str__(self):
        return f'{self.code}'
