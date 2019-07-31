import math
import functools

# class used for both vector/ vertex
class Vectex:
    def __init__(self, x, y, isVector=False):
        self._x = float(x)
        self._y = float(y)
        self._is_vector = isVector

    def __add__(self, other):
        if isinstance(other, Vectex) and self._is_vector:
            return Vectex(self._x + other._x, self._y + other._y, True)
        else:
            value = float(other)
            return Vectex(self._x + value, self._y + value, True)

    def __sub__(self, other):
        if isinstance(other, Vectex):
            return Vectex(self._x - other._x, self._y - other._y, True)
        else:
            value = float(other)
            return Vectex(self._x - value, self._y - value, True)

    def normalize(self):
        if self._is_vector:
            length = self.get_length()
            return Vectex(self._x / length, self._y / length)

    # Dot Product
    def __mul__(self, other):
        if (
            not isinstance(other, Vectex)
            or other._is_vector == False
            or self._is_vector == False
        ):
            raise ValueError("Parameter is not valid.")
        a = self.normalize()
        b = other.normalize()
        result = a._x * b._x + a._y * b._y
        return result

    def __eq__(self, other):
        if not isinstance(other, Vectex):
            return False
        if self._x == other._x and self._y == other._y:
            return True
        return False

    def get_angle_difference(self, other):
        if (
            not isinstance(other, Vectex)
            or other._is_vector == False
            or self._is_vector == False
        ):
            raise ValueError("Parameter is not valid.")
        dot_product = self * other
        return math.degrees(math.acos(dot_product))

    def get_length(self):
        if self._is_vector:
            return math.sqrt(self._x ** 2 + self._y ** 2)
        return -1


# Require: List of vertices run Clock-wise or will be error
class Polygon:
    def __init__(self, vertices):
        self._verticies = vertices
        self._size = len(vertices)
        self._area = -1
        self._perimeter = -1
        self._edges = []
        for i in range(0, self._size):
            vector = vertices[(i + 1) % self._size] - vertices[i % self._size]
            self._edges.append(vector)

    def _calculate_area(self):
        raise AttributeError("Perimeter of basic polygon can't be calculated")

    def _calculate_perimeter(self):
        self._perimeter = 0
        for i in range(0, self._size):
            self._perimeter += self._edges[i].get_length()

    def get_area(self):
        if self._area == -1:
            self._calculate_area()
        return self._area

    def get_perimeter(self):
        if self._perimeter == -1:
            self._calculate_perimeter()
        return self._perimeter

    def size(self):
        return self._size

    def __eq__(self, other):
        if not isinstance(other, Polygon) or other.size() != self.size():
            return False
        radiusOfA = []
        radiusOfB = []
        size = self.size()
        for i in range(0, size):
            radiusOfA.append(
                self._edges[i % size].get_angle_difference(self._edges[(i + 1) % size])
            )
            radiusOfB.append(
                other._edges[i % size].get_angle_difference(
                    other._edges[(i + 1) % size]
                )
            )

        for i in range(0, self.size()):
            if radiusOfB[i] not in radiusOfA:
                return False
            else:
                radiusOfA.remove(radiusOfB[i])
        return True


class Triangle(Polygon):
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise ValueError("Triangle should only have 3 vertices")
        super().__init__(vertices)

    def _calculate_area(self):
        arr = []
        p = self.get_perimeter() / 2
        arr.append(p)
        for i in self._edges:
            arr.append(p - i.get_length())
        S = functools.reduce(lambda a, b: a * b, arr)
        self._area = math.sqrt(S)


class IsoscelesTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)

        isIsosceles = False
        for i in range(0, 3):
            for j in range(i + 1, 3):
                if self._edges[i].get_length() == self._edges[j].get_length():
                    isIsosceles = True
        if not isIsosceles:
            raise ValueError("These vertices can't create a Isosceles Triangle")


class EquilateralTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)

        isEquilateral = True
        for i in range(0, 3):
            for j in range(i + 1, 3):
                if self._edges[i].get_length() != self._edges[j].get_length():
                    isEquilateral = False
        if not isEquilateral:
            raise ValueError("These vertices can't create a Isosceles Triangle")


class Quadrilateral(Polygon):
    def __init__(self, vertices):
        if len(vertices) != 4:
            raise ValueError("Quadrilateral should only have 3 vertices")
        super().__init__(vertices)

    def _calculate_area(self):
        raise AttributeError("Area of basic Quadrilateral can't be calculated")


class Rectangle(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)
        if (
            self._edges[0].get_length() != self._edges[2].get_length()
            or self._edges[0].get_angle_difference(self._edges[1]) != 90
        ):
            raise ValueError("These vertices can't create a Rectangle/Square")

    def _calculate_area(self):
        self._area = self._edges[0].get_length() * self._edges[1].get_length()


class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        if self._edges[0].get_length() != self._edges[1].get_length():
            raise ValueError("These vertices can't create a Rectangle/Square")


class EquilateralPolygon(Polygon):
    def __init__(self, vertices):
        super().__init__(vertices)

        self._a = self._edges[0].get_length()
        for i in range(0, self._size):
            b = self._edges[i].get_length()
            if self._a != b:
                raise ValueError("These vertex can't create a Equilateral Polygon")


class Pentagon(EquilateralPolygon):
    def __init__(self, vertices):
        super().__init__(vertices)

    def _calculate_area(self):
        self._area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (self._a ** 2)


class Hexagon(EquilateralPolygon):
    def __init__(self, vertices):
        super().__init__(vertices)

    def _calculate_area(self):
        self._area = ((3 * math.sqrt(3)) / 2) * (self._a ** 2)


class Octagon(EquilateralPolygon):
    def __init__(self, vertices):
        super().__init__(vertices)

    def _calculate_area(self):
        self._area = 2 * (1 + math.sqrt(2)) * (self._a ** 2)


if __name__ == "__main__":
    vex1 = Vectex(0.0, 3.0)
    vex2 = Vectex(0.0, 0.0)
    vex3 = Vectex(3.0, 0.0)
    vex8 = Vectex(3.0, 3.0)
    poly = Square([vex1, vex2, vex3, vex8])
    vex4 = Vectex(0.0 + 3.0, 3.0 + 3.0)
    vex5 = Vectex(0.0 + 3.0, 0.0 + 3.0)
    vex6 = Vectex(3.0 + 3.0, 0.0 + 3.0)
    vex9 = Vectex(3.0 + 3.0, 3.0 + 3.0)
    poly2 = Square([vex4, vex5, vex6, vex9])

    # Angle will be reversed so it should be angle - 90 if angle > 90
    print(poly == poly2)
    # print(poly.get_perimeter())
    # print(poly.get_area())

