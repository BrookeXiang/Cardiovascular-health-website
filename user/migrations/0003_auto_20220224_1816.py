# Generated by Django 2.0.7 on 2022-02-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220224_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthinformation',
            name='i_age',
            field=models.CharField(default='0', max_length=250, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_diastolicpress',
            field=models.CharField(default='0', max_length=250, verbose_name='舒张压'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_drink',
            field=models.CharField(default='0', max_length=250, verbose_name='是否饮酒'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_sex',
            field=models.CharField(default='0', max_length=250, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_smoke',
            field=models.CharField(default='0', max_length=250, verbose_name='是否吸烟'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_sport',
            field=models.CharField(default='0', max_length=250, verbose_name='是否运动'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_statur',
            field=models.CharField(default='0', max_length=250, verbose_name='身高'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_systolicpress',
            field=models.CharField(default='0', max_length=250, verbose_name='收缩压'),
        ),
        migrations.AlterField(
            model_name='healthinformation',
            name='i_weight',
            field=models.CharField(default='0', max_length=250, verbose_name='体重'),
        ),
    ]
