"""Appels HTTP vers l'API Open-Meteo (gratuite, sans clé)."""
import requests

from meteocli.models import Place

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT = 10


class WeatherError(Exception):
    """Erreur fonctionnelle (ville introuvable, réseau, ...)."""


def _get_json(url: str, params: dict) -> dict:
    try:
        response = requests.get(url, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        raise WeatherError(f"Erreur réseau : {exc}") from exc


def geocode(city: str) -> Place:
    data = _get_json(GEOCODING_URL, {"name": city, "count": 1, "language": "fr"})
    results = data.get("results")
    if not results:
        raise WeatherError(f"Ville introuvable : {city}")
    r = results[0]
    return Place(r["name"], r.get("country", ""), r["latitude"], r["longitude"])


def fetch_forecast(latitude: float, longitude: float, days: int) -> dict:
    return _get_json(
        FORECAST_URL,
        {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m,weather_code",
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code",
            "timezone": "auto",
            "forecast_days": days,
        },
    )