import binascii
print("type the encoded messsage here")
encoded = "01100011"
b = binascii.a2b_uu(encoded)
binascii.b2a_uu(b)
print(b)
