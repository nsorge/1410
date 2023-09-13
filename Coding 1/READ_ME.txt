I used this assignment to understand how recursion works instead of using the itertool "permutations" 
function that could have been used. Essentially the code takes a word and turns it into a list of 
individual characters. It recursively calls itself while incrementing start until start is equal to 
the length of the word and prints it. As the recursive calls close out it swaps the character at 
the index equal to start with the index of i. Ususally this does nothing until you return to the 
first call that is not recursive. At this point i and start will be differing values and it will 
swap the characters at the respective indexes of i and start. It is also set to return the list 
to its original order after it prints all the permutations of the word with the current character 
at the front.

This was a fun assignment and it gave me the opportunity to step through a program over and over 
until I understood the concept of recursion, which is very tricky and still hard to wrap my 
head around. For the creative element I used a dictionary to make key and value pairs of 
commmon "l33t speak" changes. the l33t_speak function enumerates the input_word list and 
compares each character with the keys in the dictionary and makes the change if applicable.

Use the word "haxor" for a good example.
