b = list(range(20))
print(b)

print(b[::2]) #get the even number by slicing
b = list(range(0, 20, 2)) #get the even number by generating a variable (from 0 to 18)
b = list(range(0, 20, -2)) #get the even number by generating a variable (from 18 to 0)
print(b)
print(b[::-1]) #the minus makes it print from larger to smaller

a = list(range(20))
print(a[5:]) #slice the list 
