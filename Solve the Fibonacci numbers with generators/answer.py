__author__ = '@AndreiNeagoie'
__PythonVersion__ = 3.9.6

def fib(number):
    a = 0  # current
    b = 1  # next number
    result = []
    for i in range(number):
        result.append(a)
        temp = a 
        a = b
        b = temp + b
    return result


print(fib(20)) # let N = 20
