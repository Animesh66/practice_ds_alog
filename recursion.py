def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)


def fibo(n):
    if n < 0:
        print("Invalid input")
    elif n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == '__main__':
    print(find_sum(5))
    print(fibo(10))
