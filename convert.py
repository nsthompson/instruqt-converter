import rich_click as click

from converters import convert_to_dev, convert_to_prod


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
    # Convert Track
    if convert_to == "dev":
        convert_to_dev(track_path, identifier)

    if convert_to == "prod":
        convert_to_prod(track_path, identifier)


if __name__ == "__main__":
    convert_track()  # pylint: disable=no-value-for-parameter
