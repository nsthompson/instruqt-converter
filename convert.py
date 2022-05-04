import logging
import rich_click as click
from rich.console import Console
from rich.logging import RichHandler

from core import config
from converters import convert_to_dev, convert_to_prod


FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")


# Collect track path at runtime
@click.command()
@click.option(
    '--track',
    'track_path',
    required=True,
    type=click.Path(exists=True, writable=True, readable=True),
    help='Path to Instruqt track'
)
@click.option(
    '--to',
    'convert_to',
    required=True,
    type=click.Choice(['dev', 'prod'], case_sensitive=False),
    help=(
        'Convert To: '
        '[dev] - Convert to dev for testing '
        '[prod] - Convert to prod for promotion'
    )
)
@click.option(
    '--identifier',
    'identifier',
    default="dev",
    show_default=True,
    required=True,
    help='Track identifier used when converting to dev'
)
def convert_track(track_path, convert_to, identifier):
    console = Console()
    # Define settings dict
    settings = {
        "config": config,
        "console": console,
        "log": log
    }
    # Convert Track
    if convert_to == "dev":
        log.info('Converting to [dev] with identifier [%s]', identifier)
        convert_to_dev(settings, track_path, identifier)

    if convert_to == "prod":
        log.info('Converting to [prod] with identifier [%s]', identifier)
        convert_to_prod(settings, track_path, identifier)


if __name__ == "__main__":
    convert_track()  # pylint: disable=no-value-for-parameter
