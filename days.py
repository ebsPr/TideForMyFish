import datetime as dt
import pytz
class Days:

    def __init__(self):
        self.time_zone = pytz.timezone("Europe/Madrid")

    def day_before_end(self,date):
        day = (date + dt.timedelta(days=-1))
        new_date = dt.datetime.combine(day, dt.time.max)
        return self.time_zone.localize(new_date)

    def day_before_ini(self,date):
        day = (date + dt.timedelta(days=-1))
        new_date =  dt.datetime.combine(day, dt.time.min)
        return self.time_zone.localize(new_date)

    def day_after_ini(self,date):
        day = (date + dt.timedelta(days=1))
        new_date =  dt.datetime.combine(day, dt.time.min)
        return self.time_zone.localize(new_date)

    def day_after_end(self,date):
        day = (date + dt.timedelta(days=1))
        new_date =  dt.datetime.combine(day, dt.time.max)
        return self.time_zone.localize(new_date)


    def tomorrow_ini(self):
        tomorrow = (dt.datetime.now() + dt.timedelta(days=1))
        new_date = dt.datetime.combine(tomorrow, dt.time.min)
        return self.time_zone.localize(new_date)

    def tomorrow_end(self):
        tomorrow = (dt.datetime.now() + dt.timedelta(days=1))
        new_date = dt.datetime.combine(tomorrow, dt.time.max)
        return self.time_zone.localize(new_date)

    def tomorrow(self):
        new_date = (dt.datetime.now() + dt.timedelta(days=1))
        return self.time_zone.localize(new_date)

    def yesterday_end(self):
        yesterday = dt.datetime.now() + dt.timedelta(days=-1)
        new_date = dt.datetime.combine(yesterday, dt.time.max)
        return self.time_zone.localize(new_date)

    def yesterday_ini(self):
        yesterday = dt.datetime.now() + dt.timedelta(days=-1)
        new_date = dt.datetime.combine(yesterday, dt.time.min)
        return self.time_zone.localize(new_date)


    def today_ini(self):
        new_date = dt.datetime.combine(dt.datetime.now(), dt.time.min)
        return self.time_zone.localize(new_date)


    def today_end(self):
        new_date = dt.datetime.combine(dt.datetime.now(), dt.time.max)
        return self.time_zone.localize(new_date)

    def day_after_tomorrow_ini(self):
        tomorrow = (dt.datetime.now() + dt.timedelta(days=2))
        new_date = dt.datetime.combine(tomorrow, dt.time.min)
        return self.time_zone.localize(new_date)

    def day_after_tomorrow_end(self):
        tomorrow = (dt.datetime.now() + dt.timedelta(days=2))
        new_date = dt.datetime.combine(tomorrow, dt.time.max)
        return self.time_zone.localize(new_date)

    def now(self):
        new_date = dt.datetime.now()
        return self.time_zone.localize(new_date)