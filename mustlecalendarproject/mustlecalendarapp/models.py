from django.db import models
from django.urls import reverse

PLACE = (('house', '家'), ('gym', 'ジ'))


class Record(models.Model):
    date = models.DateField('日付', primary_key=True)
    place = models.CharField(verbose_name='場所', max_length=100, choices=PLACE, default='house')
    category_pectoral = models.BooleanField(verbose_name='胸筋', default=False)
    category_abs = models.BooleanField(verbose_name='腹筋', default=False)
    category_spine = models.BooleanField(verbose_name='背筋', default=False)
    category_run = models.BooleanField(verbose_name='ラン', default=False)

    def __str__(self):
        return self.date.strftime('%Y/%m/%d')

    def get_absolute_url(self):
        return reverse('app:month_with_schedule')
