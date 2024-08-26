import datetime as dt
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import pytz

from days import Days


class DataManager():
    def __init__(self):
        pass

    def verify_tide(self, data_tides, date_requested):
        self.update_string_date_to_datetime(data_tides)

        data_before = None
        for d in data_tides:
            if data_before is not None:
                date_tide_before = data_before["time"]
                date_tide_d = d["time"]
                if date_tide_before <= date_requested <= date_tide_d:
                    now_text = "up"
                    tide_text = "subiendo"
                    extreme_text = "pleamar"
                    if data_before["type"] == "high" and d["type"] == "low":
                        now_text = "down"
                        tide_text = "bajando"
                        extreme_text = "bajamar"

                    return {
                        "now": now_text,
                        "tide": d,
                        "date": date_tide_d,
                        "message": {
                            "tide": tide_text,
                            "extreme": extreme_text
                        }
                    }
            data_before = d


    def update_string_date_to_datetime(self, data):
        date_utils = Days()

        for value in data:
            print(f"before {value['time']}")
            date = dt.datetime.fromisoformat(value["time"]).astimezone(date_utils.time_zone)
            print(f"after {date.hour} - {date.strftime('%H:%M')}")
            value['time'] = date

    def generate_table_weather(self, values,day):
        new_values = []

        self.update_string_date_to_datetime(values)

        for value in values:
            date = value["time"]
            now = day
            if date.month == now.month and date.year == now.year and date.day == now.day:
                new_values.append(value)


        values_morning = [item for item in new_values if 9 <= item['time'].hour <= 12]  # 8 a 12
        values_midday = [item for item in new_values if 12 < item['time'].hour <= 16]  # 12 a 16
        values_afternoon = [item for item in new_values if 16 < item['time'].hour <= 20]  # 16 a 20
        values_night = [item for item in new_values if 20 < item['time'].hour <= 23]  # de 20 a 00

        air_temperature_morning = [item["airTemperature"]["noaa"] for item in values_morning]
        print([f"air temperature morning - {item['time'].hour}: {item['airTemperature']['noaa']}" for item in values_morning])
        air_temperature_midday = [item["airTemperature"]["noaa"] for item in values_midday]
        print([f"air temperature midday - {item['time'].hour}: {item['airTemperature']['noaa']}" for item in values_midday])
        air_temperature_afternoon = [item["airTemperature"]["noaa"] for item in values_afternoon]
        print([f"air temperature afternoon - {item['time'].hour}: {item['airTemperature']['noaa']}" for item in values_afternoon])
        air_temperature_night = [item["airTemperature"]["noaa"] for item in values_night]
        print([f"air temperature night - {item['time'].hour}: {item['airTemperature']['noaa']}" for item in values_night])

        water_temperature_morning = [item["waterTemperature"]["meto"] for item in values_morning]
        print([f"water temperature morning - {item['time'].hour}: {item['waterTemperature']['meto']}" for item in values_morning])
        water_temperature_midday = [item["waterTemperature"]["meto"] for item in values_midday]
        print([f"water temperature midday - {item['time'].hour}: {item['waterTemperature']['meto']}" for item in values_midday])
        water_temperature_afternoon = [item["waterTemperature"]["meto"] for item in values_afternoon]
        print([f"water temperature afternoon - {item['time'].hour}: {item['waterTemperature']['meto']}" for item in values_afternoon])
        water_temperature_night = [item["waterTemperature"]["meto"] for item in values_night]
        print([f"water temperature night - {item['time'].hour}: {item['waterTemperature']['meto']}" for item in values_night])

        cloud_cover_morning = [item["cloudCover"]["noaa"] for item in values_morning]
        print([f"cloud cover morning - {item['time'].hour}: {item['cloudCover']['noaa']}" for item in values_morning])
        cloud_cover_midday = [item["cloudCover"]["noaa"] for item in values_midday]
        print([f"cloud cover midday - {item['time'].hour}: {item['cloudCover']['noaa']}" for item in values_midday])
        cloud_cover_afternoon = [item["cloudCover"]["noaa"] for item in values_afternoon]
        print([f"cloud cover afternoon - {item['time'].hour}: {item['cloudCover']['noaa']}" for item in values_afternoon])
        cloud_cover_night = [item["cloudCover"]["noaa"] for item in values_night]
        print([f"cloud cover night - {item['time'].hour}: {item['cloudCover']['noaa']}" for item in values_night])

        humidity_morning = [item["humidity"]["noaa"] for item in values_morning]
        print([f"humidity morning - {item['time'].hour}: {item['humidity']['noaa']}" for item in values_morning])
        humidity_midday = [item["humidity"]["noaa"] for item in values_midday]
        print([f"humidity midday - {item['time'].hour}: {item['humidity']['noaa']}" for item in values_midday])
        humidity_afternoon = [item["humidity"]["noaa"] for item in values_afternoon]
        print([f"humidity afternoon - {item['time'].hour}: {item['humidity']['noaa']}" for item in values_afternoon])
        humidity_night = [item["humidity"]["noaa"] for item in values_night]
        print([f"humidity night - {item['time'].hour}: {item['humidity']['noaa']}" for item in values_night])

        precipitation_morning = [item["precipitation"]["noaa"] for item in values_morning]
        print([f"precipitation morning - {item['time'].hour}: {item['precipitation']['noaa']}" for item in values_morning])
        precipitation_midday = [item["precipitation"]["noaa"] for item in values_midday]
        print([f"precipitation midday - {item['time'].hour}: {item['precipitation']['noaa']}" for item in values_midday])
        precipitation_afternoon = [item["precipitation"]["noaa"] for item in values_afternoon]
        print([f"precipitation afternoon - {item['time'].hour}: {item['precipitation']['noaa']}" for item in values_afternoon])
        precipitation_night = [item["precipitation"]["noaa"] for item in values_night]
        print([f"precipitation night - {item['time'].hour}: {item['precipitation']['noaa']}" for item in values_night])

        windSpeed_morning = [item["windSpeed"]["noaa"] for item in values_morning]
        print([f"wind speed morning - {item['time'].hour}: {item['windSpeed']['noaa']}" for item in values_morning])
        windSpeed_midday = [item["windSpeed"]["noaa"] for item in values_midday]
        print([f"wind speed midday - {item['time'].hour}: {item['windSpeed']['noaa']}" for item in values_midday])
        windSpeed_afternoon = [item["windSpeed"]["noaa"] for item in values_afternoon]
        print([f"wind speed afternoon - {item['time'].hour}: {item['windSpeed']['noaa']}" for item in values_afternoon])
        windSpeed_night = [item["windSpeed"]["noaa"] for item in values_night]
        print([f"wind speed night - {item['time'].hour}: {item['windSpeed']['noaa']}" for item in values_night])


        data = [
            {
                "mediciones": "Temp. Aire (ºC)",
                "Mañana\n(9:00-12:00)": round(sum(air_temperature_morning) / len(air_temperature_morning),2),
                "Mediodia\n(12:00-16:00)": round(sum(air_temperature_midday) / len(air_temperature_midday),2),
                "Tarde\n(16:00-20:00)": round(sum(air_temperature_afternoon) / len(air_temperature_afternoon),2),
                "Noche\n(20:00-23:00)": round(sum(air_temperature_night) / len(air_temperature_night),2),
            },
            {
                "mediciones": "Temp. Agua (ºC)",
                "Mañana\n(9:00-12:00)": round(sum(water_temperature_morning) / len(water_temperature_morning),2),
                "Mediodia\n(12:00-16:00)": round(sum(water_temperature_midday) / len(water_temperature_midday),2),
                "Tarde\n(16:00-20:00)": round(sum(water_temperature_afternoon) / len(water_temperature_afternoon),2),
                "Noche\n(20:00-23:00)": round(sum(water_temperature_night) / len(water_temperature_night),2),
            },
            {
                "mediciones": "Nubosidad (%)",
                "Mañana\n(9:00-12:00)": round(sum(cloud_cover_morning) / len(cloud_cover_morning),2),
                "Mediodia\n(12:00-16:00)": round(sum(cloud_cover_midday) / len(cloud_cover_midday),2),
                "Tarde\n(16:00-20:00)": round(sum(cloud_cover_afternoon) / len(cloud_cover_afternoon),2),
                "Noche\n(20:00-23:00)": round(sum(cloud_cover_night) / len(cloud_cover_night),2),
            },
            {
                "mediciones": "Lluvia (mm/h)",
                "Mañana\n(9:00-12:00)": round(sum(precipitation_morning) / len(precipitation_morning),2),
                "Mediodia\n(12:00-16:00)": round(sum(precipitation_midday) / len(precipitation_midday),2),
                "Tarde\n(16:00-20:00)": round(sum(precipitation_afternoon) / len(precipitation_afternoon),2),
                "Noche\n(20:00-23:00)": round(sum(precipitation_night) / len(precipitation_night),2),
            },
            {
                "mediciones": "Humedad (%)",
                "Mañana\n(9:00-12:00)": round(sum(humidity_morning) / len(humidity_morning),2),
                "Mediodia\n(12:00-16:00)": round(sum(humidity_midday) / len(humidity_midday),2),
                "Tarde\n(16:00-20:00)": round(sum(humidity_afternoon) / len(humidity_afternoon),2),
                "Noche\n(20:00-23:00)": round(sum(humidity_night) / len(humidity_night),2),
            },
            {
                "mediciones": "Viento (m/s)",
                "Mañana\n(9:00-12:00)": round(sum(windSpeed_morning) / len(windSpeed_morning),2),
                "Mediodia\n(12:00-16:00)": round(sum(windSpeed_midday) / len(windSpeed_midday),2),
                "Tarde\n(16:00-20:00)": round(sum(windSpeed_afternoon) / len(windSpeed_afternoon),2),
                "Noche\n(20:00-23:00)": round(sum(windSpeed_night) / len(windSpeed_night),2),
            }
        ]

        df = pd.DataFrame(data)
        matplotlib.use('agg')  # backend

        plt.clf()
        plt.close('all')
        plt.figure(figsize=(15, 4))

        ax = plt.gca()
        ax.axis('off')

        # Crea la tabla con pandas y matplotlib
        table = plt.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

        table.set_fontsize(12)

        table.scale(0.9, 2.5)  # Ajusta el factor de escala según sea necesario

        # Guarda la tabla como una imagen (por ejemplo, jpg)
        plt.savefig('tabla_tiempo.jpg', bbox_inches='tight', pad_inches=0.5)
        # plt.show()


    def generate_graph_tide(self, data, date):
        matplotlib.use('agg')  # backend
        plt.clf()
        plt.close('all')

        plt.rc('font', size=8)

        # graph data
        data_for_graph = [{
            "height": item["height"],
            "date": item["time"]
        } for item in data]

        # data axis
        data_x = [item["date"].timestamp() for item in data_for_graph]
        data_y = [item["height"] for item in data_for_graph]

        plt.plot(data_x, data_y)

        # axis labels
        data_x_labels = [f"{item['date'].strftime('%H:%M')}h" for item in data_for_graph]
        plt.xticks(data_x, data_x_labels)
        plt.ylabel('Altura en metros')

        # styling
        plt.title(f"Mareas {date.strftime('%d/%m/%Y')}")
        plt.style.use('ggplot')

        days_utils = Days()
        day_before = days_utils.day_before_end(date).timestamp()
        day_after = days_utils.day_after_ini(date).timestamp()
        plt.axvline(x=day_before, color='gray', label='axvline - full height')
        plt.axvline(x=day_after, color='gray', label='axvline - full height')

        plt.savefig('mareas.jpg')
        # plt.show()

    def get_correct_tides(self, data, date):

        self.update_string_date_to_datetime(data)

        date_utils = Days()
        day_before_end = date_utils.day_before_end(date)
        print(f"day_before_end {day_before_end}")
        day_after_start = date_utils.day_after_ini(date)
        print(f"day_after_start {day_after_start}")


        yesterday_tides = [item for item in data if item["time"] <= day_before_end]
        tomorrow_tides = [item for item in data if item["time"] >= day_after_start]
        today_tides = [item for item in data if data if day_before_end <= item["time"] <= day_after_start]
        result = []

        if len(yesterday_tides) > 0:
            result.append(yesterday_tides.pop())

        result = result + today_tides

        if len(tomorrow_tides) > 0:
            result.append(tomorrow_tides[0])
        print(result)
        return result
