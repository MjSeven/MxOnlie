from django.db import models
from django.contrib.auth.models import AbstractUser


class UserPrrofile(AbstractUser):
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    # 性别 只能男或女，默认女
    gender = models.CharField(
        max_length=5,
        verbose_name=u"性别",
        choices=GENDER_CHOICES,
        default="female")
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default="image/default.png",
        max_length=100
    )

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


