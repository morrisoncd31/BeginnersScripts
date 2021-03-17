import base64

secret = input("Please enter your deepest, darkest secret: ")
encoded = base64.b64encode(secret.encode("utf-8"))
decoded = base64.b64decode(encoded)
print("The encoded string is ", encoded)
print("The decoded string is ", decoded)
