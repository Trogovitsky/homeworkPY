a = 2
b = 3
for i in range(5, 10):
    a = a + 3 + a // 3
    b = b + a - b // 4
    print(a + b)
