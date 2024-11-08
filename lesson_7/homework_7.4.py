
def common_elements():
    a = range(0, 100, 3)
    b = range(0, 100, 5)
    return set(a).intersection(b)

common_elements()
