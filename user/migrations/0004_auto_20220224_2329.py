# Generated by Django 2.0.7 on 2022-02-24 23:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220224_1816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='healthinformation',
            options={'verbose_name': 'information', 'verbose_name_plural': 'information'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': 'user', 'verbose_name_plural': 'user'},
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_age',
            field=models.CharField(default='0', max_length=250, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_bloodglucose',
            field=models.CharField(default='0', max_length=250, verbose_name='bloodglucose'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_cholesterol',
            field=models.CharField(default='0', max_length=250, verbose_name='holesterol'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_diastolicpress',
            field=models.CharField(default='0', max_length=250, verbose_name='iastolicpress'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_drink',
            field=models.CharField(default='0', max_length=250, verbose_name='drink'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_sex',
            field=models.CharField(default='0', max_length=250, verbose_name='sex'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_smoke',
            field=models.CharField(default='0', max_length=250, verbose_name='smoke'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_sport',
            field=models.CharField(default='0', max_length=250, verbose_name='sport'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_statur',
            field=models.CharField(default='0', max_length=250, verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_systolicpress',
            field=models.CharField(default='0', max_length=250, verbose_name='systolicpress'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='time'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='ser'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_weight',
            field=models.CharField(default='0', max_length=250, verbose_name='weight'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_address',
            field=models.CharField(default='', max_length=100, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_logo',
            field=models.FileField(default='default.jpg', upload_to='images', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_name_passOrfail',
            field=models.BooleanField(default=True, verbose_name='submit'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_phone',
            field=models.CharField(default='', max_length=11, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_postcode',
            field=models.CharField(default='', max_length=6, verbose_name='mail'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_pwd',
            field=models.CharField(max_length=40, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_realname',
            field=models.CharField(default='', max_length=20, verbose_name='name'),
        ),
    ]
