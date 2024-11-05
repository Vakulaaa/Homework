
import keyword
import string


def mu_func(input_string):
    if input_string in keyword.kwlist and input_string[0].isdigit:
        return False

    if input_string.count('_') > 1:
        return False

    for char in input_string:
        if char.isupper() or char in string.punctuation.replace("_", "") or char.isspace():
            return False
    return True

