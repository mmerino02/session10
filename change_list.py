a = [1, 2, 3, 4, 5]
print(a[1])
a[1] = 33
print(a)

a = [1, 2, 3, 4, 5]
b = a
a[1] = 33
b[1] = 44
print(a, b)