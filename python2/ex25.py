def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)  # pop quita o valor da lista, e ademais podo levarmo nunha variable
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and the last one."""
    word = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


# IMPORT:

# Like this, I need to specify the source when calling a function
# import ex25 as ex25
# ex25.break_words(args)

# I can use asterisk to import all funcs without requiring specifying the source
# from ex25 import *
# break_words(args)

# whatever object defined (module, class, func, method... etc) i can call help() as
# help(ex25) # which will return all funcs in this module with their """ description
