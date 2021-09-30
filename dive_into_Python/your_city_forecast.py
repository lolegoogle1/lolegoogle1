import argparse
import requests

"""
Hello. Here you can get to know the weather in your city for a present day. 

How to use program: 
run python your_city_forecast.py with these arguments
    --city={your city in lowercase} --measure_system={imperial or metric}
"""


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--city',
                        help='Enter your city name',
                        type=str
                        )
    parser.add_argument(
                        '--measure_system',
                        help='You should specify measure'
                             ' system for view: metric or imperial',
                        type=str
                        )
    return parser.parse_args()


def city_info(args):  # args is a dict
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&" \
          "units={}&" \
          "appid=992de75a2bea2c7" \
          "c4cb8873440fe83a2".format(args['city'], args['units'])
    print(url)
    return url


def forecast_info(f_data):
    temp_info = {
                    "min_temp": f_data["main"]["temp_min"],
                    "max_temp": f_data["main"]["temp_max"],
                    "avg_temp": f_data["main"]["temp"],
                    "feels_like": f_data["main"]["feels_like"]
    }
    forecast = f"Hello. Here is a weather forecast for today in your" \
               f" city: An average temperature is going to be:" \
               f" {temp_info['avg_temp']}, " \
               f"but it would feels like {temp_info['feels_like']}. " \
               f"Besides, here is minimal and max temperature for today:" \
               f" min_t= {temp_info['min_temp']}, " \
               f"max_t = {temp_info['max_temp']}." \
               f" And by the way - Have a nice day!"
    return forecast


def get(url):
    data = requests.get(url, timeout=30).json()
    return data


def main():
    args = parse()
    url_inf = {
            "city": args.city,
            'units': args.measure_system
    }
    f_data = get(city_info(url_inf))
    print(forecast_info(f_data))


if __name__ == "__main__":
    main()
