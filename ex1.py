# Use turtle graphics to make an infinite spiral
from turtle import *
f = forward
r = right

# repeat infinite 

def vale():
    move = 0.6
    while True: 
            move = move - 2
            f(move)
            r(90)
            f(move)
vale()
