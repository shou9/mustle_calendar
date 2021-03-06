# Generated by Django 3.1.7 on 2021-04-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mustlecalendarapp', '0002_auto_20210402_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='category',
        ),
        migrations.AddField(
            model_name='record',
            name='category_abs',
            field=models.CharField(default='unchecked', max_length=100),
        ),
        migrations.AddField(
            model_name='record',
            name='category_pectoral',
            field=models.CharField(default='unchecked', max_length=100),
        ),
        migrations.AddField(
            model_name='record',
            name='category_run',
            field=models.CharField(default='unchecked', max_length=100),
        ),
        migrations.AddField(
            model_name='record',
            name='category_spine',
            field=models.CharField(default='unchecked', max_length=100),
        ),
        migrations.AddField(
            model_name='record',
            name='place',
            field=models.CharField(choices=[('house', '家'), ('gym', 'ジム')], default='house', max_length=100),
        ),
    ]
