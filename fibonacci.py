def fibo(n):
    first = 0
    second = 1
    result = 0
    if n <= 0:
        print("number cannot be negative")
    else:
        for i in range(n):
            print(result)
            first = second
            second = result
            result = first + second

fibo(5)

