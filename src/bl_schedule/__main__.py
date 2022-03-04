"""Command-line interface."""
import click
from zmanim.util.geo_location import GeoLocation
from zmanim.zmanim_calendar import ZmanimCalendar

tzais_ops = {'degrees': 6}


@click.command()
@click.version_option()
def main() -> None:
    """BL Schedule."""
    location = GeoLocation(
        'Baltimore, MD', 39.363840, -76.698372, 'America/New_York'
    )
    calendar = ZmanimCalendar(geo_location=location)
    print(calendar.tzais(tzais_ops))


if __name__ == "__main__":
    main(prog_name="bl-schedule")  # pragma: no cover
