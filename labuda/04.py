def mayfunction(n):
    return lambda a: a * n
mydubler = myfunction(2)
print(mydubler(11))