a = int(input("Enter number:"))
Amount_0s = 0
while True:
    if a % 10 == 0:
        Amount_0s += 1
    a = a / 10
    if a % 10 != 0:
        break
print(Amount_0s)
