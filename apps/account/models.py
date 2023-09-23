from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Поле «Номер телефона» должно быть заполнено.')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=15, unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number


class User(models.Model):
    ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    discussions = models.IntegerField(default=0)
    liked_discussions = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def increase_rating(self):
        # Увеличиваем рейтинг пользователя на 1
        self.rating += 1
        self.save()

    def decrease_rating(self):
        # Уменьшаем рейтинг пользователя на 1
        self.rating -= 1
        self.save()

    def update_rating(self, diff):
        # Обновляем рейтинг пользователя на указанное значение diff
        self.rating += diff
        self.save()