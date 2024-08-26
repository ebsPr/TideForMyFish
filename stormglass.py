import requests
import datetime as dt
from days import Days
import pytz

class StormGlass:

    def __init__(self, api_key: str, endpoint: str):
        self.API_KEY = api_key
        self.ENDPOINT = endpoint
        self.LAT_LAGOS = '42.325'
        self.LON_LAGOS = '-8.825'

    def fetch_tide_today_lagos(self):
        date_utils = Days()
        return self.fetch_tide(
            date_utils.yesterday_ini().timestamp(),
            date_utils.tomorrow_end().timestamp()
        )

    def fetch_tide_tomorrow(self):
        date_utils = Days()
        return self.fetch_tide(date_utils.today_ini().timestamp(), date_utils.day_after_tomorrow_end().timestamp())


    def fetch_weather(self,start,end):
        parameters = {
            "lat": self.LAT_LAGOS,
            "lng": self.LON_LAGOS,
            "start": start.timestamp(),
            "end": end.timestamp(),
            "params": "airTemperature,cloudCover,humidity,precipitation,waterTemperature,windSpeed"
        }
        headers = {
            "Authorization": self.API_KEY
        }
        response = requests.get(f"{self.ENDPOINT}/weather/point",params=parameters,headers=headers)
        print(f"response: {response.json()}")
        return response.json()["hours"]


    def fetch_tide(self, start, end):
        print("date start", start)
        print("date end", end)
        parameters = {
            "lat": self.LAT_LAGOS,
            "lng": self.LON_LAGOS,
            "start": start,
            "end": end
        }
        print("parameters", parameters)
        headers = {
            "Authorization": self.API_KEY
        }
        response = requests.get(f"{self.ENDPOINT}/tide/extremes/point", params=parameters, headers=headers)
        response.raise_for_status()
        print("response", response.json())
        data = response.json()["data"]

        return data
