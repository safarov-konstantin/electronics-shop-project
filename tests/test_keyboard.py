from src.keyboard import Keyboard
import pytest


@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init(kb):
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_setter(kb):
    with pytest.raises(AttributeError):
        kb.language = 'CH'


def test_change_lang(kb):
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
