'''
Use max, min, and sorted along with key functions to implement the
following functions and make the tests pass.

>>> most_spaces(["a", "a b", "a b c", "c", "abc"])
'a b c'

>>> one_line_poems = [
...      "The dogs are barking at the stillness, the stillness is still.",
...      "In the canopy of the night heaven the stars are tiptoeing.",
...      "A sunrise smiles wide into my expectant face.",
...      "The bees are awakening to the life in a yellow wonder!",
...      "The land runs astoundingly under my soles.",
...      "The dance of the flowers kissed by the butterflies.",
... ]

>>> fewest_vowels(one_line_poems)
'The land runs astoundingly under my soles.'

>>> most_consonants(one_line_poems)
'The dogs are barking at the stillness, the stillness is still.'

>>> for poem in sorted_by_word_count(one_line_poems):
...     print(poem)
The land runs astoundingly under my soles.
A sunrise smiles wide into my expectant face.
The dance of the flowers kissed by the butterflies.
The dogs are barking at the stillness, the stillness is still.
In the canopy of the night heaven the stars are tiptoeing.
The bees are awakening to the life in a yellow wonder!

EXTRA CREDIT:
Once you get this lab to pass, read about lambda expressions in the
Python docs:
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions 

Modify your code to use lambda expressions instead of separately defined key functions.

'''

# Write your code here:
# def most_spaces(items):
#     def num_space(s):
#         return s.count(" ")
#     return max(items, key=num_space)

def most_spaces(items):
    return max(items, key=lambda s: s.count(" "))

def count_char(s, subset):
    count = 0
    for c in s.lower():
        if c in subset:
            count += 1
    return count

def count_vowels(s):
    return count_char(s, "aeiou")

def count_consonants(s):
    return count_char(s, "bcdfghjklmnpqrstvwxyz")

def fewest_vowels(one_line_poems):
    return min(one_line_poems, key=count_vowels)

def most_consonants(one_line_poems):
    return max(one_line_poems, key=count_consonants)

def word_count(s):
    return len(s.split(" "))

def sorted_by_word_count(one_line_poems):
    return sorted(one_line_poems, key=lambda s: len(s.split())


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
