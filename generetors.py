# This note is about to Generator""""

import time
def fib(num):
    a=1
    b=1
    for n in range(num):
         yield b
         a,b = b,a+b

'''
gen= fib(40)
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))

'''
for n in fib(10000):
    print (n)

'''
def fib(num):
    result=[]
    a=1
    b=1
    for n in range(num):
         a,b = b,a+b
         result.append(b)
    return result

print(fib(10000))'''
