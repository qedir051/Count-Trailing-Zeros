def count_zeros(a):
    Amount_0s = 0
    while True:
        if a % 10 == 0:
            Amount_0s += 1
        a = a // 10
        if a % 10 != 0:
            break
    return Amount_0s

number = int(input("Enter number:"))
zeros_count = count_zeros(number)
print(zeros_count)
