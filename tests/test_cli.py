from click.testing import CliRunner

from instruqt_converter.convert import convert_track


def test_cli_help_lists_options():
    result = CliRunner().invoke(convert_track, ["--help"])
    assert result.exit_code == 0
    assert "--track" in result.output
    assert "--to" in result.output


def test_cli_requires_track_argument():
    result = CliRunner().invoke(convert_track, [])
    assert result.exit_code != 0
