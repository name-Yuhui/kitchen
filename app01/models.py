from djongo import models

# class News(models.Model):
#     title = models.CharField(verbose_name="标题",max_length=50)
#     author = models.CharField(verbose_name="作者",max_length=10)
#     desc = models.CharField(verbose_name="简介",max_length=100)
#     content = models.TextField(verbose_name="正文")
#     create_time = models.DateTimeField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True,auto_now_add=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = '新闻'
#         verbose_name_plural = verbose_name