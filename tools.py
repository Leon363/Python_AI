import requests

URL = 'https://api.apilayer.com/fixer/latest'
API_KEY = 'ZVV5eRhcelfZXLqluJwFeYrjaGrR9UjK'

URL_WEATHER = 'https://openweathermap.org'
API_KEY_WEATHER = '5202c33d2c43a7472190c5409cbc66c9'

if not API_KEY or not API_KEY_WEATHER:
    raise RuntimeError("API_KEY is not set")


def get_exchange_rate(from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    try:
        resp = requests.get(URL, params={'base': from_currency, 'symbols': to_currency}, headers={'apikey': API_KEY})
    except requests.RequestException:
        return f"Could not reach the exchange rate service to check {from_currency} to {to_currency}"
    data = resp.json()
    if resp.status_code != 200 or not data.get('success', True):
        return f"Could not get exchange rate for {from_currency} to {to_currency}"
    rate = data.get('rates', {}).get(to_currency)
    if rate is None:
        return f"{to_currency} is not valid currency"

    return f"one {from_currency} = {rate} {to_currency}"

def get_weather(city):
    try:
        params = {
            'appid': API_KEY_WEATHER,
            'q': city,
            'units': 'metric',
            'lang': 'en',
        }
        resp = requests.get(URL_WEATHER, params=params)
    except requests.RequestException:
        return f"Could not reach the weather service to check {city}"

    if resp.status_code == 401:
        return f'Wrong API key'
    elif resp.status_code != 404:
        return f"Could not get weather data for {city}"
    elif resp.status_code != 200:
        return f"Mistake for get weather data for {city}"

    data = resp.json()

    location_name = data.get('name', city)
    temp_c = data.get('main', {}).get('temp', 'N/A')
    weather_list = data.get('weather', [])
    condition = weather_list[0].get('description', 'unknown') if weather_list else 'unknown'

    return f'Weather in {location_name}:\n{temp_c} C,\n{condition}'


TOOLS = {
    'get_exchange_rate': get_exchange_rate,
    'get_weather': get_weather,
}