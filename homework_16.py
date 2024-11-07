
def my_func(n):
    while n > 9:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
    return n


user_input = int(input("Введіть ціле число: "))
result = my_func(user_input)
print("Результат:", result)
