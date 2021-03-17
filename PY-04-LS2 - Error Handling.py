product = 1
for i in range(4):
    try:
        num = int(input("Enter a number: "))
        product *= num
    except:
        print("Nah, nah nah... that number's not valid.")
print("The product of the four numbers is "+ str(product))
