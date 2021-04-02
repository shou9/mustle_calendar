from django.contrib import admin
from django.urls import path
from .views import MonthWithScheduleCalendar, ScheduleCreate

app_name = 'app'

urlpatterns = [
    path('', MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('month_with_schedule/<int:year>/<int:month>/', MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('create/', ScheduleCreate.as_view(), name='create')
]
