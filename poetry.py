import random

poem = """
I have half my father's face
& not a measure of his flair
for the dramatic. Never once
have I prayed & had another man's wife
wail in return.
"""
 
list_of_lines = poem.split("\n")

# Your code should implement the lines_printed_backwards() function. 
# This function takes in a list of strings containing the lines of your 
# poem as arguments and will print the poem lines out in reverse with the line numbers reversed. 

def lines_printed_backwards(list_of_lines):
    for lines in list_of_lines:
        list_of_lines.reverse()
    print(list_of_lines)

def lines_printed_random(list_of_lines):
    """Your code should implement the lines_printed_random() function which will randomly select lines from a list of strings and print them out in random order. Repeats are okay and the number of lines printed should be equal to the original number of lines in the poem (line numbers don't need to be printed). Hint: try using a loop and randint()"""

    for lines in list_of_lines:
        print(random.choice(list_of_lines))

def my_costum_function(list_of_lines):
    """"Your code should implement a function of your choice that rearranges the poem in a unique way, be creative! Make sure that you carefully comment your custom function so it's clear what it does."""
    # IT's going to delete the last line
    for lines in list_of_lines:
        list_of_lines.pop()
    print(list_of_lines)

lines_printed_backwards(list_of_lines)
lines_printed_random(list_of_lines)
my_costum_function(list_of_lines)
