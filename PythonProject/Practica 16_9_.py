# Заданине 16.9.1; 16.9.2
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Прямоугольник {self.x}, {self.y}, {self.width}, {self.height}'

    def get_area(self):
        return self.x * self.y


r1 = Rectangle(5, 6, 10, 15)
print(r1)
print(f'Площадь фигуры = {r1.get_area()}')


# Заданине 16.9.3; 16.9.4
class Client:
    def __init__(self, name, second_name="", city="", balance=0):
        self.name = name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'Клиент - "{self.name} {self.second_name}. {self.city}. Баланс: {self.balance} руб."'

    def get_guest_list(self):
        return f'Клиент - "{self.name} {self.second_name}. {self.city}."'


client_1 = Client('Иван', "Пупкин", "Тольятти", 150)
client_2 = Client('Гадя', "Петрова", "Урюпинск", 200)
client_3 = Client('Генри', "Форд", "Детройт", 3300)

guest_list = [client_1, client_2, client_3]

for i in guest_list:
    print(i.get_guest_list())