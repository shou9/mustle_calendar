# Generated by Django 3.1.7 on 2021-04-04 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mustlecalendarapp', '0009_auto_20210404_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(unique=True, verbose_name='日付'),
        ),
    ]
