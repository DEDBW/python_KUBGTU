class Shape:
    def __init__(self, identifier):
        self.identifier = identifier

    def area(self):
        raise NotImplementedError("Подклассы должны реализовывать метод area")


class Rectangle(Shape):
    def __init__(self, identifier, x, y, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами")
        super().__init__(identifier)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Quad(Rectangle):  # Квадрат — это частный случай прямоугольника
    def __init__(self, identifier, x, y, side):
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть положительным числом")
        super().__init__(identifier, x, y, side, side)


def compare(t1, t2):
    """Сравнивает объекты по площади"""
    area1 = t1.area()
    area2 = t2.area()
    if area1 > area2:
        return f"{t1.identifier} больше чем {t2.identifier}"
    elif area1 < area2:
        return f"{t1.identifier} меньше чем {t2.identifier}"
    else:
        return f"{t1.identifier} и {t2.identifier} равны по площади"


def is_intersect(t1, t2):
    if (t1.x + t1.width <= t2.x or t2.x + t2.width <= t1.x or
            t1.y + t1.height <= t2.y or t2.y + t2.height <= t1.y):
        return "Объекты не пересекаются"
    return "Объекты пересекаются"


# Пример использования
rect = Rectangle("Прямоугольник", 0, 0, 4, 6)
quad = Quad("Квадрат", 2, 2, 3)

print(compare(rect, quad))  # Сравнение
print(is_intersect(rect, quad))  # Проверка пересечения
