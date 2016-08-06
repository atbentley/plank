import pytest
from plank import cli


def test_end_to_end(monkeypatch):
    monkeypatch.setattr('plank.Inspector.DEFAULT_PLANKS_MODULE_NAME', 'tests.fixtures.sample_planks')

    with pytest.raises(ValueError):
        cli.main(['raises_value_error'])
