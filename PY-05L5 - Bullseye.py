import random

def generate_random():
    number = random.randint(1, 10)
    return(number)

def main():
    guessed_number = int(input("Please select a number b/w 1 and 10: "))
    random_number = generate_random()
    if guessed_number == random_number:
        print("You guessed it!")
    else:
        print("You suck at guessing!")

if __name__ == "__main__":
    main()