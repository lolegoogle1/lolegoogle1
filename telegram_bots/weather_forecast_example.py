import requests


class CityInfo:
    def __init__(self, name='lviv', units='metric'):
        self.name = name.lower()
        self.units = units
        self._forecast_provider = WeatherForecast()

    def get_forecast(self):
        return self._forecast_provider.get_(self.name, self.units)


class WeatherForecast:
    def __init__(self):
        self._cashed_data = {}

    def get_(self, city, units):
        # if city in self._cashed_data.keys():
        #   return self._cashed_data[city]
        url = f"http://api.openweathermap.org/data/2.5/weather?" \
              f"q={city}&units={units}" \
              f"&appid=992de75a2bea2c7c4cb8873440fe83a2"
        print("sending HTTP request")
        data = requests.get(url, timeout=30).json()
        temp_info = {
            "min_temp": data["main"]["temp_min"],
            "max_temp": data["main"]["temp_max"],
            "avg_temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"]
        }
        forecast = f"Hello. Here is a weather forecast for today in your" \
                   f" city: An average temperature is going to be:" \
                   f" {temp_info['avg_temp']}, " \
                   f"but it would feels like {temp_info['feels_like']}. " \
                   f"Besides, here is minimal and max temperature for today:" \
                   f" min_t= {temp_info['min_temp']}, " \
                   f"max_t = {temp_info['max_temp']}." \
                   f" And by the way - Have a nice day!"
        # self._cashed_data[city] = temp_info
        return forecast

    def forecast_cash(self):
        pass

