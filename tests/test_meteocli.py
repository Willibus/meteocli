from click.testing import CliRunner

from meteocli import cli
from meteocli.api import WeatherError
from meteocli.models import Place, parse_forecast
from meteocli.weather_codes import describe_code

SAMPLE = {
    "current": {"temperature_2m": 12.5, "wind_speed_10m": 8.0, "weather_code": 3},
    "daily": {
        "time": ["2026-11-13", "2026-11-14"],
        "temperature_2m_min": [5.0, 6.0],
        "temperature_2m_max": [13.0, 14.0],
        "precipitation_sum": [0.0, 2.5],
        "weather_code": [3, 61],
    },
}


def test_describe_code_known_and_unknown():
    assert describe_code(0) == "Ciel dégagé"
    assert describe_code(12345) == "Inconnu"


def test_parse_forecast():
    current, days = parse_forecast(SAMPLE)
    assert current.temperature == 12.5
    assert len(days) == 2
    assert days[1].precipitation == 2.5


def test_cli_success(monkeypatch):
    monkeypatch.setattr(cli, "geocode", lambda city: Place("Lyon", "France", 45.7, 4.8))
    monkeypatch.setattr(cli, "fetch_forecast", lambda lat, lon, days: SAMPLE)
    result = CliRunner().invoke(cli.main, ["Lyon", "--days", "2"])
    assert result.exit_code == 0
    assert "Lyon" in result.output


def test_cli_city_not_found(monkeypatch):
    def boom(city):
        raise WeatherError("Ville introuvable : xxx")

    monkeypatch.setattr(cli, "geocode", boom)
    result = CliRunner().invoke(cli.main, ["xxx"])
    assert result.exit_code == 1
    assert "introuvable" in result.output