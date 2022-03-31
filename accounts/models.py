from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AuthUserManager(BaseUserManager):
    def create_user(self, username, password,):
        """
        ユーザ作成

        :param username: ユーザID
        :param password: パスワード
        :return: AuthUserオブジェクト
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(username=username,
                          password=password,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password,):
        """
        スーパーユーザ作成

        :param username: ユーザID
        :param password: パスワード
        :return: AuthUserオブジェクト
        """
        user = self.create_user(username=username,
                                password=password,)
        user.admin = True
        user.save(using=self._db)
        return user


class AuthUser(AbstractBaseUser):
    class Meta:
        db_table = 'user'
        verbose_name = 'User'

        """
        ユーザ設定

        :param username: ユーザID
        :param date_joined: 追加された日
        :param admin: 管理者フラグ
        :param password: パスワード
        :param last_login: 最後にログインした日時
        """
    username = models.CharField(verbose_name='ユーザID',
                                unique=True, null=False,
                                max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)

    admin = models.BooleanField(verbose_name='管理サイトアクセス権限', default=False)

    password = models.CharField(max_length=1024, null=True)

    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = 'username'

    objects = AuthUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.admin

    @property
    def date_joined(self):
        return self.date_joined
