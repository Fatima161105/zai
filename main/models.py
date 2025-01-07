from django.db import models

class Products(models.Model):
    name= models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug=models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description =models.TextField(blank=True,null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='index_images', blank=True, null=True, verbose_name='Изображение')
    price=models.DecimalField(default =0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount=models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity=models.PositiveIntegerField(default=0, verbose_name='Количество')


    class Meta:
        db_table: str = 'product'
        verbose_name: str='Продукт'
        verbose_name_plural: str ='Продукты'

    def __str__(self) -> str:
        return f'{self.name} Количество -{self.quantity}'