# make infinite circles, start with a small circle, then draw a bigger circle around it

from turtle import *

r = 1
while True:
    r = r * 2
    circle(r)
