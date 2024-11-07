
def correct_sentence(text):
    text = text.replace(",", ".")
    if not text.endswith("."):
        text+= "."
    print(text.title())

correct_sentence("greetings, friends")