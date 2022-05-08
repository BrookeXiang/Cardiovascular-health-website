from django.db import models

from datetime import datetime



class UserInfo(models.Model):

    u_name = models.CharField(max_length=20, verbose_name="用户名", unique=True)
    u_logo= models.FileField(verbose_name="用户头像",upload_to='images', default='default.jpg')
    u_pwd = models.CharField(max_length=40, verbose_name="用户密码", blank=False)
    u_email = models.EmailField(verbose_name="邮箱", unique=True)
    u_realname = models.CharField(max_length=20, default="", verbose_name="真实姓名")
    u_address = models.CharField(max_length=100, default="", verbose_name="地址")
    u_postcode = models.CharField(max_length=6, default="", verbose_name="邮编")
    u_phone = models.CharField(max_length=11, default="", verbose_name="手机号")
    u_name_passOrfail = models.BooleanField(verbose_name="允许登录", default=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uname

class HealthInformation(models.Model):

    i_age = models.CharField(max_length=250, verbose_name="年龄")
    i_sex = models.CharField(max_length=250, verbose_name="性别")
    i_statur = models.CharField(max_length=250, verbose_name="身高")
    i_weight = models.CharField(max_length=250, verbose_name="体重")
    i_systolicpress = models.CharField(max_length=250, verbose_name="收缩压")
    i_diastolicpress = models.CharField(max_length=250, verbose_name="舒张压")
    i_bloodglucose = models.CharField(max_length=250, verbose_name="血糖")
    i_smoke = models.CharField(max_length=250, verbose_name="是否吸烟")
    i_drink = models.CharField(max_length=250, verbose_name="是否饮酒")
    i_sport = models.CharField(max_length=250, verbose_name="是否运动")
    i_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="消息")

    class Meta:
        verbose_name = "健康信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cusername1

