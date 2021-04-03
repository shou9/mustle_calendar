from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .mixins import MonthCalendarMixin, MonthWithScheduleMixin
from .models import Record
from bootstrap_datepicker_plus import DateTimePickerInput


class MonthWithScheduleCalendar(MonthWithScheduleMixin, TemplateView):
    template_name = 'month.html'
    model = Record

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class ScheduleCreate(CreateView):
    template_name = 'create.html'
    model = Record
    fields = ('date', 'place', 'category_pectoral', 'category_abs', 'category_spine', 'category_run')
    success_url = reverse_lazy('app:month_with_schedule')

    def get_form(self):
        form = super().get_form()
        form.fields['date'].widget = DateTimePickerInput(format='%Y-%m-%d')
        return form
