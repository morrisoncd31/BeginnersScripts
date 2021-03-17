try:
    num1 = int(input("Please enter a number: "))
    num2 = 5
    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("Can't calculate that.")
except ValueError:
    print("Oh snap bro, uou broke it!")