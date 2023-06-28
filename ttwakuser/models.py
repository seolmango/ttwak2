from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, nickname, auth_type, password=1111):

        if not email:
            raise ValueError('must have user email')
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            auth_type=auth_type
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, auth_type, password):

        user = self.create_user(
            email=email,
            nickname=nickname,
            auth_type=auth_type,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    object = UserManager()

    # 유저 정보
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        max_length=25,
        null=False,
        unique=True,
    )
    auth_type = models.IntegerField(
        null=False,
        default=0,
    )

    # 시스템 변수
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email', 'auth_type']
