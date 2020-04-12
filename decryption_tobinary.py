
print("type the encoded messsage here")
encoded = input()
array = []

for x in encoded:
    if x == 'G':
        y = x.replace("G", "0")

        array.append(y)
    elif x == 'T':
        y = x.replace("T", "1")

        array.append(y)
    elif x == 'C':
        y = x.replace("C", "0")

        array.append(y)
    elif x == 'A':
        y = x.replace("A", "1")

        array.append(y)
    else:
        print("DISGUSTANG")
        break

a = "".join(array)    # join everything into 1 string
print(a)

n = 8
output = [a[i:i+n] for i in range(0, len(a), n)]      # splice into groups of 8

print(output)
