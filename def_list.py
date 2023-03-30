a = []
print(f"a is {a}, type of a={type(a)}")

a = [1, 2, 3, 4]
print(a)
b = [3.3, -9, 0, 11, "bob"]
print(b)
c = [1, 1.2, 0, True, "xxxx", print, None]
print(c)

print(b[1]) #select only one item
c[5](b[1])
print(c[-1])
print(len(c))
d = a + b
print(d)

d = 3*a
print(d)
d = [a, a, a, a]
print(d, d[2][2])
