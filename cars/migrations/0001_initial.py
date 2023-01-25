# Generated by Django 4.1.5 on 2023-01-24 13:41

import cars.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Марка автомобиля (например, BMW)', max_length=50, unique=True, verbose_name='Марка')),
                ('icon', models.ImageField(blank=True, help_text='Иконка марки автомобиля', null=True, upload_to=cars.utils.directory_image_path, verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Марка',
                'verbose_name_plural': 'Марки',
                'db_table': 'brands',
                'ordering': ['-title'],
            },
        ),
    ]
