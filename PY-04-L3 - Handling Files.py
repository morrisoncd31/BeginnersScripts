try:
    with open("text.txt", "r") as text:
        text.write("Test")

except Exception:
    print("Bro, you can't write in read mode. You know this.")