from django.db import models

from datetime import datetime



class UserInfo(models.Model):

    u_name = models.CharField(max_length=20, verbose_name="username", unique=True)
    u_pwd = models.CharField(max_length=40, verbose_name="password", blank=False)
    u_email = models.EmailField(verbose_name="email", unique=True)
    u_realname = models.CharField(max_length=20, default="", verbose_name="name")
    u_address = models.CharField(max_length=100, default="", verbose_name="address")
    u_postcode = models.CharField(max_length=6, default="", verbose_name="mail")
    u_phone = models.CharField(max_length=11, default="", verbose_name="phone")
    u_name_passOrfail = models.BooleanField(verbose_name="submit", default=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.u_name

class HealthInformation(models.Model):

    i_age = models.IntegerField(default='0', verbose_name="age")
    i_sex = models.IntegerField(default='0', verbose_name="sex")
    i_statur = models.FloatField(max_length=250, default='0', verbose_name="height")
    i_weight = models.FloatField(max_length=250, default='0', verbose_name="weight")
    i_systolicpress = models.FloatField(max_length=250, default='0', verbose_name="systolicpress")
    i_diastolicpress = models.FloatField(max_length=250, default='0', verbose_name="iastolicpress")
    i_cholesterol = models.FloatField(max_length=250, default='0', verbose_name="holesterol")
    i_bloodglucose = models.FloatField(max_length=250, default='0', verbose_name="bloodglucose")
    i_smoke = models.IntegerField(default='0', verbose_name="smoke")
    i_drink = models.IntegerField(default='0', verbose_name="drink")
    i_sport = models.IntegerField(default='0', verbose_name="sport")
    i_time = models.DateTimeField(verbose_name="time", default=datetime.now)
    i_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="ser")

    class Meta:
        verbose_name = "information"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.i_user.u_name)

