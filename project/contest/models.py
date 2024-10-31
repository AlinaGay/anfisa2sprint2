from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


class Contest(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.TextField('Описание',  max_length=200)
    price = models.IntegerField(
        'Цена',
        validators=[MinValueValidator(10), MaxValueValidator(100)],
        help_text='Рекомендованная розничная цена'
    )
    comment = models.TextField(
        'Комментарий',
        blank=True,
        max_length=200
    )
