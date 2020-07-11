cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    n0 = 0
    n1 = 1
    fibonacciList=[]
    for i in range(n):
        fibonacciList.append(n0)
        sum = n0 + n1
        n0 = n1
        n1 = sum
    return fibonacciList


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
