from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image= models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone= models.CharField(max_length=20, unique=True, verbose_name='Номер телефона')

    class Meta:
        db_table: str = 'user'
        verbose_name: str='Пользователя'
        verbose_name_plural: str ='Пользователи'


    def __str__(self) -> str:
        return self.username