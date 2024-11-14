
def first_word(text: str):
    """ Поиск первого слова """
    text = "".join(i for i in text if i.isalpha() or i ==" ")
    splitted_text = text.split(" ")
    word = (splitted_text[0])
    return word

first_word("hello, my best friend!")
