#
# import string
#
#
# def my_hashtag(my_string):
#     new_string = "".join(char for char in my_string if char not in string.punctuation).split()
#     hashtag = "#" + "".join(word.capitalize() for word in new_string)
#     print(hashtag[:140])
#
# my_hashtag("my little pony")