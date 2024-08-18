from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from apps.common.models import BaseModel


class CustomManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError('Email did not come')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not password:
            raise TypeError('Password did not come')
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.is_verified = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    phone_number = models.CharField(max_length=225, null=True, blank=True, db_index=True, unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(unique=True, db_index=True, max_length=50)
    is_author = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = CustomManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [EMAIL_FIELD]

    def __str__(self):
        if self.get_full_name():
            return f"{self.id} - {self.get_full_name()}"
        return self.email

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class VerifyEmail(models.Model):
    email = models.EmailField(unique=True, db_index=True, max_length=50)
    code = models.CharField(max_length=6, verbose_name="Verify code")

    class Meta:
        verbose_name = "Confirm Email"
        verbose_name_plural = "Confirm Emails"

    def __str__(self) -> str:
        return f"{self.email}"
