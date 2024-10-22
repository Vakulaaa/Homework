
a = [12, 3, 4, 10]
if a[-1] in a:
    b = a.pop()
    a.insert(0, b)
    print(a)
else:
    a = []
    print(a)
