class Car:
    def __init__(self, color, windows_number, price):
        self.color = color
        self.windows_number = windows_number
        self.price = price

car1 = Car("Red", 4, 100000)
car2 = Car("Blue", 2, 300500)

print(car1.color)
print(car2.price)

