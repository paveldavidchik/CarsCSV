
import os
import codecs
import csv


class CarBase:
    """Базовый класс для всех автомобилей"""
    def __init__(self, car_type: str = '', photo_file_name: str = '', brand: str = '', carrying: float = 0.0):
        """
        :param car_type:               Тип атомобиля
        :param photo_file_name:        Путь к фотографии автомобиля
        :param brand:                  Марка автомобиля
        :param carrying:               Грузоподъемность автомобиля
        """
        if isinstance(car_type, str):
            self.__car_type = car_type
        else:
            self.__car_type = ''
        if isinstance(photo_file_name, str):
            self.__photo_file_name = photo_file_name
        else:
            self.__photo_file_name = ''
        if isinstance(brand, str):
            self.__brand = brand
        else:
            self.__brand = ''
        if isinstance(carrying, float):
            self.__carrying = carrying
        else:
            self.__carrying = ''

    """Геттер и сеттер атрибута car_type"""
    car_type = property()

    @car_type.setter
    def car_type(self, car_type: str):
        try:
            if not isinstance(car_type, str):
                raise ValueError('Неверный тип автомобиля')
            else:
                self.__car_type = car_type
        except ValueError as err:
            print(err)

    @car_type.getter
    def car_type(self) -> str:
        return self.__car_type

    """Геттер и сеттер атрибута photo_file_name"""
    photo_file_name = property()

    @photo_file_name.setter
    def photo_file_name(self, photo_file_name: str):
        try:
            if not isinstance(photo_file_name, str):
                raise ValueError('Неверный путь к фотографии автомобиля')
            else:
                self.__photo_file_name = photo_file_name
        except ValueError as err:
            print(err)

    @photo_file_name.getter
    def photo_file_name(self) -> str:
        return self.__photo_file_name

    """Геттер и сеттер атрибута brand"""
    brand = property()

    @brand.setter
    def brand(self, brand: str):
        try:
            if not isinstance(brand, str):
                raise ValueError('Неверная марка автомобиля')
            else:
                self.__brand = brand
        except ValueError as err:
            print(err)

    @brand.getter
    def brand(self) -> str:
        return self.__brand

    """Геттер и сеттер атрибута carrying"""
    carrying = property()

    @carrying.setter
    def carrying(self, carrying: float):
        try:
            if not isinstance(carrying, float):
                raise ValueError('Грузоподъемность должна быть числом')
            else:
                self.__carrying = carrying
        except ValueError as err:
            print(err)

    @carrying.getter
    def carrying(self) -> float:
        return self.__carrying

    def get_photo_file_ext(self) -> str:
        """Возвращает расширение файла изображения автомобиля"""
        try:
            return os.path.splitext(self.__photo_file_name)[1]
        except TypeError:
            print('Неверный путь к файлу изображения автомобиля')

    def __str__(self) -> str:
        return f'car_type={self.__car_type}, photo_file_name={self.__photo_file_name}, brand={self.__brand}, carrying={self.__carrying}'


class Car(CarBase):
    """Класс, представляющий легковой автомобиль"""
    def __init__(self, photo_file_name: str = '', brand: str = '', carrying: float = 0.0,
                 passenger_seats_count: int = 0):
        """
        :param passenger_seats_count:    Колличество пассажирских мест
        """
        super(Car, self).__init__('car', photo_file_name, brand, carrying)
        try:
            if not isinstance(passenger_seats_count, int) or passenger_seats_count < 0:
                raise ValueError
            else:
                self.__passenger_seats_count = passenger_seats_count
        except ValueError:
            print('Неверное колличество пассажирских мест! Значение устанавливается в 0')
            self.__passenger_seats_count = 0

    """Геттер и сеттер атрибута passenger_seats_count"""
    passenger_seats_count = property()

    @passenger_seats_count.setter
    def passenger_seats_count(self, passenger_seats_count: int):
        try:
            if not isinstance(passenger_seats_count, int) or passenger_seats_count < 0:
                raise ValueError
            else:
                self.__passenger_seats_count = passenger_seats_count
        except ValueError:
            print('Неверное колличество пассажирских мест!')

    @passenger_seats_count.getter
    def passenger_seats_count(self) -> int:
        return self.__passenger_seats_count

    def __str__(self) -> str:
        return f'{super(Car, self).__str__()}, passenger_seats_count={self.__passenger_seats_count}'


class Truck(CarBase):
    """Класс, представляющий грузовой автомобиль"""
    def __init__(self, photo_file_name: str = '', brand: str = '', carrying: float = 0.0,
                 body_whl: str = ''):
        """
        :param body_whl: Строка, представляющая габариты автомобиля, разделянные латинской буквой x
        """
        super(Truck, self).__init__('truck', photo_file_name, brand, carrying)
        try:
            self.__body_length, self.__body_width, self.__body_height = [float(num) for num in body_whl.split('x')]
        except ValueError:
            print('Неверные габариты автомобиля! Все значения устанавливаются в 0.0')
            self.__body_length, self.__body_width, self.__body_height = 0.0, 0.0, 0.0

    """Геттер и сеттер атрибута body_whl"""
    body_whl = property()

    @body_whl.setter
    def body_whl(self, body_whl: str):
        try:
            self.__body_length, self.__body_width, self.__body_height = [float(num) for num in body_whl.split('x')]
        except ValueError:
            print('Неверные габариты автомобиля!')

    @body_whl.getter
    def body_whl(self) -> str:
        return 'x'.join(map(str, [self.__body_length, self.__body_width, self.__body_height]))

    def get_body_volume(self) -> float:
        """Возвращает объем кузова"""
        return self.__body_length * self.__body_width * self.__body_height

    def __str__(self) -> str:
        return f'{super(Truck, self).__str__()}, body_whl={self.body_whl}'


class SpecMachine(CarBase):
    """Класс, представляющий спецтехнику"""
    def __init__(self, photo_file_name: str = '', brand: str = '', carrying: float = 0.0,
                 extra: str = ''):
        """
        :param extra:        Дополнительное описание автомобиля
        """
        super(SpecMachine, self).__init__('spec_machine', photo_file_name, brand, carrying)
        try:
            if not isinstance(extra, str):
                raise ValueError
            else:
                self.__extra = extra
        except ValueError:
            print('Неверное дополнительное описание автомобиля!')
            self.__extra = ''

    """Геттер и сеттер атрибута extra"""
    extra = property()

    @extra.setter
    def extra(self, extra: str):
        try:
            if not isinstance(extra, str):
                raise ValueError
            else:
                self.__extra = extra
        except ValueError:
            print('Неверное дополнительное описание автомобиля!')

    @extra.getter
    def extra(self) -> str:
        return self.__extra

    def __str__(self) -> str:
        return f'{super(SpecMachine, self).__str__()}, extra={self.__extra}'


def get_car_list(csv_file: str) -> list:
    """Функция получает в качестве аргумента путь к файлу csv с таблицей автомобилей и возвращает список автомобилей"""
    car_list = []
    try:
        with codecs.open(csv_file, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                if row['car_type'] == 'car':
                    car_list.append(Car(row['photo_file_name'], row['brand'], float(row['carrying']), int(row['passenger_seats_count'])))
                elif row['car_type'] == 'truck':
                    car_list.append(Truck(row['photo_file_name'], row['brand'], float(row['carrying']), row['body_whl']))
                elif row['car_type'] == 'spec_machine':
                    car_list.append(SpecMachine(row['photo_file_name'], row['brand'], float(row['carrying']), row['extra']))
    except FileNotFoundError:
        print('Файл не найден!')
    return car_list


for car in get_car_list('cars.csv'):
    print(car)
