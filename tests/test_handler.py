from instruqt_converter.converters.utils.handler import YAMLHandler


def test_yaml_handler_roundtrip():
    handler = YAMLHandler()
    metadata = {"slug": "my-track", "title": "My Track", "type": "challenge"}
    loaded = handler.load(handler.export(metadata))
    assert loaded == metadata


def test_yaml_handler_multiline_uses_block_scalar():
    handler = YAMLHandler()
    metadata = {"description": "line one\nline two\nline three"}
    exported = handler.export(metadata)
    assert "|" in exported  # multiline strings use YAML block style
    loaded = handler.load(exported)
    assert loaded["description"].strip() == metadata["description"]
