from django.shortcuts import render
from django.views import generic
from .mixins import MonthCalendarMixin, MonthWithScheduleMixin
from .models import Record


class MonthWithScheduleCalendar(MonthWithScheduleMixin, generic.TemplateView):
    template_name = 'month.html'
    model = Record

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context
