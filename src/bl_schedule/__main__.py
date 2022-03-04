"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """BL Schedule."""


if __name__ == "__main__":
    main(prog_name="bl-schedule")  # pragma: no cover
