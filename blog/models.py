from django.core.exceptions import ValidationError
from django.db import models
from PIL import Image
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        unique=True,
    )
    body = models.TextField(
        verbose_name='Текст',
    )
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение',
        help_text='Изображение должно быть в формате jpg или png и разрешением больше FullHD',
    )
    middle_title = models.CharField(
        max_length=255,
        verbose_name='Заголовок второго блока (необязательно)',
        blank=True,
        null=True,
    )
    middle_body = models.TextField(
        verbose_name='Текст второго блока (необязательно)',
        blank=True,
        null=True,
    )
    middle_image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение второго блока (необязательно)',
        help_text='Изображение должно быть в формате jpg или png и разрешением больше FullHD',
        blank=True,
        null=True,

    )
    last_title = models.CharField(
        max_length=255,
        verbose_name='Заголовок третьего блока (необязательно)',
        blank=True,
        null=True,
    )
    last_body = models.TextField(
        verbose_name='Текст третьего блока (необязательно)',
        blank=True,
        null=True,
    )

    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name='Слаг',
        unique=True,
        help_text='Уникальное значение для URL. Используйте только латинские символы, цифры, дефисы и знаки подчеркивания.'
    )

    # валидация изображения
    def clean(self):
        if self.image:
            image = Image.open(self.image)
            width, height = image.size
            if width < 1920 or height < 1080:
                raise ValidationError('Разрешение изображения должно быть больше FullHD')
        if self.middle_image:
            image = Image.open(self.middle_image)
            width, height = image.size
            if width < 1920 or height < 1080:
                raise ValidationError('Разрешение изображения должно быть больше FullHD')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + '...'  # 100 characters

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def image_url(self):
        return self.image.url

    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
