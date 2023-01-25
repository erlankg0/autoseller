from django.db import models
from cars.utils import directory_image_path


class Brand(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Марка',
        help_text='Марка автомобиля (например, BMW)',
        unique=True,
    )
    icon = models.ImageField(
        upload_to=directory_image_path,
        verbose_name='Иконка',
        help_text='Иконка марки автомобиля',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'
        ordering = ['title']
        db_table = 'brands'
