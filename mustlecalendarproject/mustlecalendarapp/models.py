from django.db import models

PLACE = (('house', '家'), ('gym', 'ジム'))


class Record(models.Model):
    date = models.DateField('日付')
    place = models.CharField(max_length=100, choices=PLACE, default='house')
    category_pectoral = models.CharField(max_length=100, default='unchecked')
    category_abs = models.CharField(max_length=100, default='unchecked')
    category_spine = models.CharField(max_length=100, default='unchecked')
    category_run = models.CharField(max_length=100, default='unchecked')

    def __str__(self):
        return self.date.strftime('%Y/%m/%d')
