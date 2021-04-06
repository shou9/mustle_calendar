from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from .mixins import MonthCalendarMixin, MonthWithScheduleMixin
from .models import Record
from bootstrap_datepicker_plus import DateTimePickerInput
import datetime
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout


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
    fields = ('date', 'place', 'category_pectoral', 'category_abs', 'category_spine', 'category_run', 'user')
    success_url = reverse_lazy('app:month_with_schedule')

    def get_form(self):
        form = super().get_form()
        form.fields['date'].widget = DateTimePickerInput(format='%Y-%m-%d')
        form.fields['place'].widget.attrs["style"] = "margin-left: 70px"
        form.fields['category_pectoral'].widget.attrs["style"] = "margin-left: 95px"
        form.fields['category_abs'].widget.attrs["style"] = "margin-left: 95px"
        form.fields['category_spine'].widget.attrs["style"] = "margin-left: 95px"
        form.fields['category_run'].widget.attrs["style"] = "margin-left: 95px"

        return form

    def get_initial(self):
        initial = super().get_initial()
        initial["date"] = datetime.date.today()
        return initial


class ScheduleUpdate(UpdateView):
    template_name = 'update.html'
    model = Record
    fields = ('place', 'category_pectoral', 'category_abs', 'category_spine', 'category_run')
    success_url = reverse_lazy('app:month_with_schedule')

    def get_form(self):
        form = super().get_form()
        form.fields['place'].widget.attrs["style"] = "margin-left: 70px"
        form.fields['category_pectoral'].widget.attrs["style"] = "margin-left: 95px"
        form.fields['category_abs'].widget.attrs["style"] = "margin-left: 95px"
        form.fields['category_spine'].widget.attrs["style"] = "margin-left: 95px"
        form.fields['category_run'].widget.attrs["style"] = "margin-left: 95px"

        return form


class ScheduleDetail(DetailView):
    template_name = 'detail.html'
    model = Record
    fields = ('date', 'place', 'category_pectoral', 'category_abs', 'category_spine', 'category_run')
    success_url = reverse_lazy('app:month_with_schedule')


def delete_data(request, pk):
    if request.method == 'POST':
        Record.objects.filter(id=pk).delete()
    return redirect('app:month_with_schedule')


def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        # userが重複している場合にエラーをだす
        try:
            user = User.objects.create_user(username_data, '', password_data)
            return redirect('app:login')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています。'})

    return render(request, 'signup.html', {})


def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('app:month_with_schedule')
        else:
            return render(request, 'login.html', {'error': 'ユーザー名、またはパスワードが違います。'})
    return render(request, 'login.html')


def logoutview(request):
    logout(request)
    return redirect('app:login')
