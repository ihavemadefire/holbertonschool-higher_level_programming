#!/usr/bin/python3
def multiple_returns(sentence):

    l = len(sentence)
    if l < 1:
        first = "None"
    else:
        first = sentence[0]
    return(l, first)
