a = int(input("Введите число:"))
b = -1
while a > 10:
    c = a % 10
    a //= 10
    if c > b:
        b = c
print(b)