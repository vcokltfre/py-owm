# py-owm

## A Python library to interface with the OpenWeatherMap weather API

Example:
```py
from py_owm import OWMClient

client = OWMClient("your_api_token")

weather = client.get_by_name("London")

print(weather.raw)
```