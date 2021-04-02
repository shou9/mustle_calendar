from django.shortcuts import render
from django.views import generic
from .mixins import MonthCalendarMixin


class MonthCalendar(MonthCalendarMixin, generic.TemplateView):
    template_name = 'month.html'

    # 選択中の年と月を引数にとる
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context
