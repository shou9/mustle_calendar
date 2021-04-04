from django.contrib import admin
from django.urls import path
from .views import MonthWithScheduleCalendar, ScheduleCreate, ScheduleUpdate, ScheduleDetail, signupview, loginview, logoutview


app_name = 'app'

urlpatterns = [
    path('', MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('month_with_schedule/<int:year>/<int:month>/', MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('create/', ScheduleCreate.as_view(), name='create'),
    path('update/<int:pk>/', ScheduleUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', ScheduleDetail.as_view(), name='detail'),
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
]
