import  pytest
from src.item import Item


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
