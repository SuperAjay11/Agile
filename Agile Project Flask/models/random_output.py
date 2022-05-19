import random

def user_input():
    words = input()
    return words

def word_list(words):
    list = words.split(" ")
    return list

def random_output(list):
    random_output = random.choice(list)
    return random_output