import pytest, os
from src.item import Item
from pathlib import Path


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount(item1, item2):
    Item.pay_rate = 0.8
    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000


def test_name(item1):
    # длина наименования товара меньше 10 символов
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'

    # Длина наименования товара больше 10 символов
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
