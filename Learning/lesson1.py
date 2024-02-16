words = ['hello', 'world', 'this', 'is', 'greath']


# def smash(words):
sentence = ""
for word in words:
    sentence = sentence + " " + word
print(sentence[1:].lstrip("h"))
