from django.apps import AppConfig


class GoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goods'
    verbose_name='Товары '

class Goods1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goods1'
    verbose_name='Товары '