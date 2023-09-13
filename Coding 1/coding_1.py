'''Permutations in l33t speak!'''

l33t_dict = {'a':'4', # Collection of common l33t corrections
             'e':'3',
             'i':'1',
             'o':'0'}


def permutations(word, start=0):
    '''Generates all permutations of a given word'''
    if start == len(word):
        print(''.join(word)) # Joins the given word list with '' and prints it as one word
    else:
        for i in range(start, len(word)):
            # Swap characters at positions start and i
            word[start], word[i] = word[i], word[start]
            # Recursively generates permutations for the remaining characters
            permutations(word, start + 1)
            # Swaps the characters back to their original positions
            word[start], word[i] = word[i], word[start]


def l33t_speak():
    '''Creative Element: Converts normal characters to l33t speak'''
    for i, val in enumerate(input_word): # Enumerates over the characters
        if val in l33t_dict:
            input_word[i] = l33t_dict[input_word[i]] # Changes character to l33t correction


input_word = input("Enter a word: ") # Input word
input_word = list(input_word)  # Converts the input string to a list of characters

l33t_speak()
permutations(input_word)
