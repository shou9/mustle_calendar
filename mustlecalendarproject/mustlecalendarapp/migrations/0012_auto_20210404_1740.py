# Generated by Django 3.1.7 on 2021-04-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mustlecalendarapp', '0011_record_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(verbose_name='日付'),
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.UniqueConstraint(fields=('user', 'date'), name='unique_date'),
        ),
    ]
