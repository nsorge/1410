'''Permutations of a word!'''


def generate_permutations(word, start=0):
    '''Generates all permutations of a given word'''
    if start == len(word):
        print(''.join(word)) # Joins the given word list with '' and prints it as one word
    else:
        for i in range(start, len(word)):
            # Swap characters at positions start and i
            word[start], word[i] = word[i], word[start]
            # Recursively generates permutations for the remaining characters
            generate_permutations(word, start + 1)
            # Swaps the characters back to their original positions
            word[start], word[i] = word[i], word[start]


# Input word
input_word = input("Enter a word: ")
input_word = list(input_word)  # Convert the input string to a list of characters

generate_permutations(input_word)
