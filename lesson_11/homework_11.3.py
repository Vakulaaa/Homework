
def is_even(num):
    num_list = ("0","2","4","6","8")
    num = str(num)
    for i in num_list:
        result = False
        if num[-1] == i:
            result = True
            return

is_even(488)
