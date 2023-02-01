from django.apps import AppConfig


class CreditConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'credit'
    verbose_name = 'Кредит и заявки'
    verbose_name_plural = 'Кредиты и заявки'
