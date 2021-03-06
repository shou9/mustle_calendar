# Generated by Django 3.1.7 on 2021-04-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mustlecalendarapp', '0004_auto_20210403_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='category_abs',
            field=models.BooleanField(default=False, verbose_name='腹筋'),
        ),
        migrations.AlterField(
            model_name='record',
            name='category_pectoral',
            field=models.BooleanField(default=False, verbose_name='胸筋'),
        ),
        migrations.AlterField(
            model_name='record',
            name='category_run',
            field=models.BooleanField(default=False, verbose_name='ラン'),
        ),
        migrations.AlterField(
            model_name='record',
            name='category_spine',
            field=models.BooleanField(default=False, verbose_name='背筋'),
        ),
    ]
