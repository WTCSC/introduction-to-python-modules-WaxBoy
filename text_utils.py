import re



def count_chars(text):
    """
    Count the number of characters in a text
    """
    kntkdl = len(text)
    return kntkdl

def count_words(text):
    """
    Count the number of words in a text
    """
    kntvlb = len(text.split())
    return kntvlb

def count_sentences(text):
    """
    Count the number of sentences in a text
    """   
    text = text.replace('?','.').replace('!','.')  #Turn punctuation to periods and count each instance
    tex = text.split('.')

    tex.pop()
    
    return len(tex)
        