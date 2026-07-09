from instruqt_converter.core.config import Settings


def test_settings_reads_env(monkeypatch):
    monkeypatch.setenv("INSTRUQT_API_URL", "https://example.com/graphql")
    monkeypatch.setenv("INSTRUQT_API_KEY", "secret-key")
    monkeypatch.setenv("INSTRUQT_ORG_SLUG", "acme")
    settings = Settings()
    assert settings.INSTRUQT_API_URL == "https://example.com/graphql"
    assert settings.INSTRUQT_API_KEY == "secret-key"
    assert settings.INSTRUQT_ORG_SLUG == "acme"


def test_settings_default_none_when_unset(monkeypatch):
    for var in ("INSTRUQT_API_URL", "INSTRUQT_API_KEY", "INSTRUQT_ORG_SLUG"):
        monkeypatch.delenv(var, raising=False)
    settings = Settings()
    assert settings.INSTRUQT_API_URL is None
    assert settings.INSTRUQT_API_KEY is None
    assert settings.INSTRUQT_ORG_SLUG is None
