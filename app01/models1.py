from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name="姓名")
    address = models.CharField("地址", max_length=50)
    gender = models.CharField(max_length=30, verbose_name="性别")
    occupation = models.CharField(max_length=30, verbose_name="职业")
    fans = models.CharField(max_length=255, verbose_name="粉丝列表",null=True)
    fans_num = models.IntegerField( verbose_name="粉丝数")
    attentions = models.CharField(max_length=255, verbose_name="关注列表",null=True)
    attentions_num = models.IntegerField( verbose_name="关注数")
    image = models.ImageField(verbose_name="头像")
    collections = models.CharField(max_length=255, verbose_name="收藏列表",null=True)

    # recipe = models.CharField(max_length=30, verbose_name="姓名")
    # works = models.CharField(max_length=30, verbose_name="作品")

    class Meta:
        verbose_name_plural = "用户"


    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=30, verbose_name="标题")
    description = models.CharField(max_length=30, verbose_name="描述")
    type = models.CharField(max_length=30, verbose_name="分类")
    collected_nums = models.CharField(max_length=30, verbose_name="标题")
    description = models.CharField(max_length=255, verbose_name="描述")
    title = models.CharField(max_length=30, verbose_name="标题")
    # foods =

    # recipe = models.CharField(max_length=30, verbose_name="姓名")
    # works = models.CharField(max_length=30, verbose_name="作品")

    class Meta:
        verbose_name_plural = "用户"


    def __str__(self):
        return self.name
