from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, first_name, last_name, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Поле «Номер телефона» должно быть заполнено.')
        user = self.model(phone_number=phone_number, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, first_name, last_name, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    rating = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_number}"

    def increase_rating(self):
        self.rating += 1
        self.save()

    def decrease_rating(self):
        self.rating -= 1
        self.save()

    def update_rating(self, diff):
        self.rating += diff
        self.save()