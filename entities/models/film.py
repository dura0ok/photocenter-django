from django.db import models


class Film(models.Model):
    code = models.CharField(
        unique=True,
        max_length=255,
        help_text='Уникальный код фильма'
    )

    class Meta:
        managed = False
        db_table = 'films'
        verbose_name = 'Фотопленка'
        verbose_name_plural = 'Фотопленки'

    def __str__(self):
        return f'{self.code}'