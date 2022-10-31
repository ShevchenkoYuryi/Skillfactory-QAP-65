from Practica_16_8_2_rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area())
print(rect_2.get_area())

squre_1 = Square(5)
squre_2 = Square(10)

print(squre_1.get_area_square())
print(squre_2.get_area_square())

circle_1 = Circle(6)
circle_2 = Circle(11)

print(circle_1.get_area_circle())
print(circle_2.get_area_circle())

print('---------------------------------')

figures = [rect_1, rect_2, squre_1, squre_2, circle_1,circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())