def factorial(num):
    p = 1
    for i in range(2, num+1):
        p *= i
    return p

def rec_fac(num):
    if num == 1:
        return 1
    return num*rec_fac(num-1)

print(rec_fac(4))

