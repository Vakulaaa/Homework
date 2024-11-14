def pow(x):
    return x**2

def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    value = begin
    for _ in range(end):
        yield value
        value = func(value)

if __name__ == "__main__":
    generator = some_gen(pow, 3, 4)