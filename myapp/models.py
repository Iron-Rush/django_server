from django.db import models

# Create your models here.
class AllInfo(models.Model):
    lottieid = models.IntegerField(primary_key=True, verbose_name="id")
    lottie = models.CharField(max_length=100, verbose_name="动图URL")
    userimg = models.CharField(max_length=100, verbose_name="用户头像")
    username = models.CharField(max_length=50, verbose_name="用户昵称")
    type = models.CharField(max_length=20, verbose_name="所属类别")

    class Meta:
        verbose_name = "图片URL数据"
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.time_info

# class MXInfo(models.Model):
#     province = models.CharField(max_length=50, verbose_name='省')
#     name = models.CharField(max_length=50, verbose_name='市')
#     confirm = models.IntegerField(verbose_name='确诊')
#     suspect = models.IntegerField(verbose_name='疑似')
#     dead = models.IntegerField(verbose_name='死亡')
#     heal = models.IntegerField(verbose_name='治愈')
#     time_info = models.DateTimeField(verbose_name='更新时间')
#
#     class Meta:
#         verbose_name = '各省信息'
#         verbose_name_plural = verbose_name
#     def __str__(self):
#         return self.time_info