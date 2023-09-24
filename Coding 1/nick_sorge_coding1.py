'''Permutations in l33t speak!'''

# Collection of common "l33t" corrections
l33t_dict = {'a':'4',
             'e':'3',
             'i':'1',
             'o':'0'}


def check_repeat(word):
    '''Checks that there are no repeated characters'''
    char = []
    for i, val in enumerate(word):
        # Checks if the current letter being evaluated is already in char list
        if val in char:
            return True
        # Adds letter to char list
        char.append(word[i])
    return False


def permutations(word, start=0):
    '''Generates all permutations of a given word'''
    if start == len(word):
        # Joins the given word list with '' and prints it as one word
        print(''.join(word))
    else:
        for i in range(start, len(word)):
            # Swap characters at positions start and i
            word[start], word[i] = word[i], word[start]
            # Recursively generates permutations for the remaining characters
            permutations(word, start + 1)
            # Swaps the characters back to their original positions
            word[start], word[i] = word[i], word[start]


def l33t_speak(word):
    '''Creative Element: Converts normal characters to "l33t speak"'''
    for i, val in enumerate(word):
        # Changes character to l33t correction if applicable
        if val in l33t_dict:
            word[i] = l33t_dict[word[i]]

def main():
    '''Main'''
    while True:
        # Prompts user for input word
        input_word = input("Enter a word: ")
        # Checks input word is all letters
        if input_word.isalpha():
            pass
        else:
            print('Only use letters in your input.')
            continue
        # Converts the input string to a list of characters
        input_word = list(input_word)
        # Checks input word for repeating characters
        if check_repeat(input_word):
            print('Try a word that does not repeat letters.')
            continue
        break
    l33t_speak(input_word)
    permutations(input_word)

if __name__ == '__main__':
    main()

# Thoughts

#This was a fun assignment and it gave me the opportunity to step through a program over and over
#until I understood the concept of recursion, which is very tricky and still hard to wrap my
#head around. For the creative element I used a dictionary to make key and value pairs of
#commmon "l33t speak" changes. the l33t_speak function enumerates the input_word list and
#compares each character with the keys in the dictionary and makes the change if applicable.
#I could not figure out how to make the try except format work because having numbers or
#repeating characters did not create a python error code I could use to except the try so
#I used if else statements instead.

#Use the word "haxor" for a good example of the programs creative element.
