'''import time
from turtle import *
from pygame import mixer

mixer.init()
mixer.music.load('ABBA - Happy New Year.mp3')
mixer.music.play(-1)
n = 100
speed("fastest")
left(90)
forward(3 * n)
color("orange", "yellow")
begin_fill()
left(126)
for i in range(5):
    forward(n / 5)
    right(144)
    forward(n / 5)
    left(72)
end_fill()
right(126)
color("dark green")
backward(n * 4.8)


def tree(d, s):
    if d <= 0:
        return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)


tree(15, n)
backward(n / 2)

time.sleep(60)
'''
help("modules")