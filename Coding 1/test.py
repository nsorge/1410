word = 'abc'
word = list(word)

word[0], word[1] = word[1], word[0]

print(word)

