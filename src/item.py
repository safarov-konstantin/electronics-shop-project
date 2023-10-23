import csv
import os
from pathlib import Path


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.massage = args[0] if args else 'Неизвестная ошибка'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity

    @property
    def name(self):
        """
        Геттер для name
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        сеттер для name
        """
        # В противном случае, обрезать строку
        self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path='src/items.csv'):
        """
        Инициализирующий экземпляры класса Item
        данными из файла по пути path
        """
        # oчищаем свойства класса all
        Item.all.clear()
        file_path = os.path.join(Path(__file__).parent.parent, path)

        # Проверка на существование файла
        if not os.path.isfile(file_path):
            raise FileNotFoundError('Отсутствует файл item.csv')

        with open(file_path) as file:
            data = csv.DictReader(file)
            try:
                [cls(**item) for item in data]
            except TypeError:
                raise InstantiateCSVError('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(str_num: str):
        """
        Возвращает число из числа-строки
        """
        return int(float(str_num))
