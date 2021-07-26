items = [
    ('product1', 10),
    ('product1', 9),
    ('product1', 19)
]

items.sort(key=lambda item: item[1])
print(items)
