counter = 0

while counter < 10:
    counter += 1
    if counter == 6:
        print("Found!")
        break
    else:
        print("Check the value is {}".format(counter))