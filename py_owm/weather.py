from copy import copy
from typing import Union

from .static import human_codes


class Weather:
    def __init__(self, data: dict):
        self.raw = copy(data)
        self.coord: dict = data.pop("coord")
        self.longitude: float = self.coord["lon"]
        self.latitude: float = self.coord["lat"]
        self.weather: list = data.pop("weather")
        self.base: str = data.pop("base")
        self.visibility: int = data.pop("visibility")
        self.wind: dict = data.pop("wind")
        self.timestamp: int = data.pop("dt")
        self.sys: dict = data.pop("sys")
        self.timezone: int = data.pop("timezone")
        self.id: int = data.pop("id")
        self.name: str = data.pop("name")
        self.cod: int = data.pop("cod")

        self.main: dict = data.pop("main")

        self.temp: float = self.main["temp"]
        self.feels_like: float = self.main["feels_like"]
        self.temp_min: float = self.main["temp_min"]
        self.temp_max: float = self.main["temp_max"]
        self.pressure: int = self.main["pressure"]
        self.humidity: int = self.main["humidity"]

        self.clouds: Union[dict, None] = data.get("clouds", None)
        self.rain: Union[dict, None] = data.get("rain", None)
        self.snow: Union[dict, None] = data.get("snow", None)

    def get_human_weather(self):
        code = self.weather[0]["id"]
        return human_codes.get(code)
