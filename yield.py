def top_ten():
    yield 1
    yield 2
    print("I'm third")
    yield 4


value = top_ten()
print(next(value))
print(next(value))
print(next(value))
