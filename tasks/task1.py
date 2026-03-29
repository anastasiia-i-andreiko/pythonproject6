class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height) / 2

    def perimeter(self):
        hypotenuse = (self.width**2 + self.height**2) ** 0.5
        return self.width + self.height + hypotenuse

w = float(input("Введіть основу трикутника: "))
h = float(input("Введіть висоту трикутника: "))

triangle = Triangle(w, h)

print("Площа =", triangle.area())
print("Периметр =", triangle.perimeter())