"""Interface en ligne de commande."""
import click
from rich.console import Console
from rich.table import Table

from meteocli.api import WeatherError, fetch_forecast, geocode
from meteocli.models import parse_forecast
from meteocli.weather_codes import describe_code


@click.command()
@click.argument("city")
@click.option("--days", default=3, type=click.IntRange(1, 7), show_default=True,
              help="Nombre de jours de prévision (1 à 7).")
@click.version_option(package_name="meteocli")
def main(city: str, days: int) -> None:
    """Affiche la météo actuelle et les prévisions pour CITY."""
    console = Console()
    try:
        place = geocode(city)
        raw = fetch_forecast(place.latitude, place.longitude, days)
    except WeatherError as exc:
        raise click.ClickException(str(exc)) from exc

    current, forecast = parse_forecast(raw)
    console.print(f"[bold]{place.name}[/bold] ({place.country})")
    console.print(
        f"Maintenant : {current.temperature} °C, vent {current.wind_speed} km/h, "
        f"{describe_code(current.code)}"
    )

    table = Table(title=f"Prévisions sur {days} jour(s)")
    for col in ("Date", "Min °C", "Max °C", "Pluie mm", "Temps"):
        table.add_column(col)
    for day in forecast:
        table.add_row(day.date, str(day.t_min), str(day.t_max),
                      str(day.precipitation), describe_code(day.code))
    console.print(table)


if __name__ == "__main__":
    main()