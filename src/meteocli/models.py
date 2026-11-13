"""Modèles de données et analyse de la réponse Open-Meteo."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Place:
    name: str
    country: str
    latitude: float
    longitude: float


@dataclass(frozen=True)
class Current:
    temperature: float
    wind_speed: float
    code: int


@dataclass(frozen=True)
class Day:
    date: str
    t_min: float
    t_max: float
    precipitation: float
    code: int


def parse_forecast(data: dict) -> tuple[Current, list[Day]]:
    """Transforme le JSON brut de l'API en objets Python."""
    cur = data["current"]
    current = Current(cur["temperature_2m"], cur["wind_speed_10m"], cur["weather_code"])
    d = data["daily"]
    days = [
        Day(date, tmin, tmax, rain, code)
        for date, tmin, tmax, rain, code in zip(
            d["time"],
            d["temperature_2m_min"],
            d["temperature_2m_max"],
            d["precipitation_sum"],
            d["weather_code"],
        )
    ]
    return current, days