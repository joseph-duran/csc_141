'''
Joseph Duran
Chapter 6
This program will show the glossary of programming of more terms.
6/10
'''
glossary = {
    'variable': 'A variable is a named location used to store data in the memory.',
    'string': 'A string is a sequence of characters.',
    'list': 'A list is a collection of items in a particular order.',
    'dictionary': 'A dictionary is a collection of key-value pairs.',
    'function': 'A function is a block of code that performs a specific task.',
    'statement': 'A statement is a line of code that performs an action.'}

for term, definition in glossary.items():

    print(f"{term.title()}: {definition}")