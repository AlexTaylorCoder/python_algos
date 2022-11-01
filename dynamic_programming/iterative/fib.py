

def fib(n):
    arr = [0] * (n+1)
    arr[1] = 1
    for i in range(n):
        arr[i+1] += arr[i]
        arr[i+2] += arr[i]
    return arr[n]


print(fib(4))