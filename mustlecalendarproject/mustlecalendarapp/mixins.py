import calendar
import datetime
import itertools


class MonthCalendarMixin:
    def __init__(self):
        self._calendar = calendar.Calendar()

    def get_previous_month(self, date):
        if date.month == 1:
            return date.replace(year=date.year-1, month=12, day=1)
        else:
            return date.replace(month=date.month-1, day=1)

    def get_next_month(self, date):
        if date.month == 12:
            return date.replace(year=date.year+1, month=1, day=1)
        else:
            return date.replace(month=date.month+1, day=1)

    def get_current_month(self):
        # urlから得られる情報
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        if month and year:
            month = datetime.date(year=int(year), month=int(month), day=1)
        else:
            month = datetime.date.today().replace(day=1)
        return month

    def get_month_days(self, date):
        return self._calendar.monthdatescalendar(date.year, date.month)

    def get_month_calendar(self):
        current_month = self.get_current_month()
        calendar_data = {
            'now': datetime.date.today(),
            'month_days': self.get_month_days(current_month),
            'month_current': current_month,
            'month_previous': self.get_previous_month(current_month),
            'month_next': self.get_next_month(current_month),
            'week_names': ['月', '火', '水', '木', '金', '土', '日'],
        }
        return calendar_data


class MonthWithScheduleMixin(MonthCalendarMixin):
    def get_month_schedules(self, start, end, days):
        query = {
            'date__range': (start, end),
            'user_id': self.request.user.id
        }
        result = self.model.objects.filter(**query)

        day_schedule = {day: [] for week in days for day in week}
        for schedule in result:
            schedule_date = getattr(schedule, 'date')
            day_schedule[schedule_date] = schedule

        size = len(day_schedule)
        # 一か月のスケジュールを7日ごとに保持
        schedule = [{key: day_schedule[key] for key in itertools.islice(day_schedule, i, i+7)} for i in range(0, size, 7)]
        return schedule

    def get_month_calendar(self):
        calendar_context = super().get_month_calendar()
        month_days = calendar_context['month_days']
        month_first = month_days[0][0]
        month_last = month_days[-1][-1]
        calendar_context['month_day_schedules'] = self.get_month_schedules(
            month_first,
            month_last,
            month_days
        )
        return calendar_context
