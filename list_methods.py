list_methods = dir([])
for method in list_methods:
    if method.startswith("__"):
        continue
    print(method)

a = [1, 2, 3]
a.append(7)
a.append("james") #adds an element to the list
print(a)
#a.clear()
#print(a)
b = a.copy() #b is a copy of a
a = [1, 1, 1, 1, 2, 2, 2, 1, 1]
print(a.count(1)) #counts the number of 1
a = ["bob", "james", "jane"]
print(a.index("jane")) #tells you in which position is the item (ex: jane = 2)
e = a.pop ()
print (e, a) #delete the last one

import random
a = []
for i in range(100):
    a.append(random.randint(1,1000))
print(a)
a.sort() #organize the list
#a.sort(reverse=True) #organize the list backwards
print(a)


