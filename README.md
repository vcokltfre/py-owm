# py-owm

## A Python library to interface with the OpenWeatherMap weather API

Examples:
```py
from py_owm import OWMClient

client = OWMClient("your_api_token")

weather = client.get_by_name("London")

print(weather.raw)
```
Async:
```py
from asyncio import get_event_loop
from py_owm import AsyncOWMClient

client = AsyncOWMClient("your_api_token")

async def main():
    weather = await client.get_by_name("London")
    print(weather.raw)
    await client.close()

loop = get_event_loop()
loop.run_until_complete(main())
```