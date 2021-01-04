from requests import get

from .weather import Weather

API_location = "https://api.openweathermap.org/data/2.5/weather"
headers = {"User-Agent":"PyOpenWeatherMap (https://github.com/vcokltfre/py-owm)"}


class OWMClient:
    def __init__(self, api_token: str):
        self.token = api_token

    def get(self, query: str):
        query += f"&appid={self.token}"

        response = get(API_location + query)
        response.raise_for_status()

        return Weather(response.json())

    def get_by_name(self, location: str, state_code: str = None, country_code: str = None) -> Weather:
        if country_code and not state_code:
            raise AttributeError("If country_code is set, state_code cannot be None.")

        state_code = f",{state_code}" if state_code else ""
        country_code = f",{country_code}" if country_code else ""

        query = f"?q={location}{state_code}{country_code}"

        return self.get(query)

    def get_by_id(self, city_id: str) -> Weather:
        return self.get(f"?id={city_id}")

    def get_by_latlong(self, latitude: float, longitude: float) -> Weather:
        return self.get(f"?lat={latitude}&lon={longitude}")

    def get_by_zip(self, zip: str, country_code: str) -> Weather:
        return self.get(f"?zip={zip},{country_code}")
