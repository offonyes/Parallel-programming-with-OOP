class Trapezoid:
    def __init__(self, trap=[0, 0, 0]):
        self.a = min(trap)
        self.b = max(trap)
        self.h = sum(trap) - (self.a + self.b)

    def area(self):
        return (self.a + self.b) / 2 * self.h

    def __str__(self):
        return f"Trapezoid: Big base -> {self.a}, Small base -> {self.b}, Height -> {self.h}"

    def __le__(self, other):
        return self.area() <= other.area() if isinstance(other, Trapezoid) else TypeError("Unsupported operand type for  <= Trapezoid and {}".format(type(other)))

    def __lt__(self, other):
        return self.area() < other.area() if isinstance(other, Trapezoid) else TypeError("Unsupported operand type for  < Trapezoid and {}".format(type(other)))


    def __ge__(self, other):
        return self.area() >= other.area() if isinstance(other, Trapezoid) else TypeError("Unsupported operand type for  >= Trapezoid and {}".format(type(other)))


    def __gt__(self, other):
        return self.area() > other.area() if isinstance(other, Trapezoid) else TypeError("Unsupported operand type for  > Trapezoid and {}".format(type(other)))


    def __eq__(self, other):
        return self.area() == other.area() if isinstance(other, Trapezoid) else TypeError("Unsupported operand type for  == Trapezoid and {}".format(type(other)))


    def __ne__(self, other):
        return self.area() != other.area() if isinstance(other, Trapezoid) else TypeError("Unsupported operand type for  != Trapezoid and {}".format(type(other)))


    def __add__(self, other):
        return self.area() + other.area() if isinstance(other, Trapezoid) else TypeError("Unsupported operand type for  + Trapezoid and {}".format(type(other)))

    def __sub__(self, other):
            return self.area() - other.area() if isinstance(other, Trapezoid) else TypeError("Unsupported operand type for  - Trapezoid and {}".format(type(other)))

    def __mod__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() % other.area() if isinstance(other, Trapezoid) else TypeError("Unsupported operand type for  % Trapezoid and {}".format(type(other)))


class Rectangle(Trapezoid):
    def __init__(self, re=None):
        if re is None:
            re = [0, 0]
        super().__init__([re[0], re[0], re[1], 0])

    def __str__(self):
        return f"Rectangle: Height -> {self.a}, Width -> {self.h}"


class Square(Rectangle):
    def __init__(self, re=None):
        if re is None:
            re = [0]
        super().__init__([re[0], re[0], re[0]])

    def __str__(self):
        return f"Square: Side -> {self.a}"



