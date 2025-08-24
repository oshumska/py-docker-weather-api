import os
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    # write your code here
    api_key = os.environ.get("API_KEY")
    paris = "Paris"
    if api_key:
        url = BASE_URL + "?key=" + api_key + "&q=" + paris
        print(f"Performing request for Weather API for city {paris}")
        response = requests.get(url)
        if response.ok:
            response = response.json()
            city = response["location"]["name"]
            country = response["location"]["country"]
            date_time_local = response["location"]["localtime"]
            temp_c = response["current"]["temp_c"]
            condition = response["current"]["condition"]["text"]

            print(f"{city}/{country}"
                  f" {date_time_local} "
                  f"Weather: {temp_c} "
                  f"Celsius, {condition}")
        else:
            print(response.json()["error"]["message"])

    else:
        print("API Key not set")


if __name__ == "__main__":
    get_weather()
