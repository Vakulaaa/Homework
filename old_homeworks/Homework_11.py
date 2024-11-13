#
# from string import ascii_letters
#
# LETTERS = ascii_letters
# SEP = "-"
#
# def MyFunc(a = str, b = str):
#     my_range = input("Write your input: ")
#     if len(my_range) == 3:
#         first_letter = my_range[0]
#         separator = my_range[1]
#         second_letter = my_range[2]
#     if first_letter.isalpha() and second_letter.isalpha() and separator == SEP:
#         first_index, second_index = LETTERS.index(first_letter), LETTERS.index(second_letter)
#         if first_index > second_index:
#             first_index, second_index = second_index, first_index
#         print(LETTERS[first_index:second_index])
# MyFunc()