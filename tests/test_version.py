import instruqt_converter


def test_version_is_nonempty_string():
    assert isinstance(instruqt_converter.__version__, str)
    assert instruqt_converter.__version__
