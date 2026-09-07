import turtle
s = turtle.getscreen()
t = turtle.Turtle()

def r(length):
    t.fd(length)
    t.rt(90)

def l(length):
    t.fd(length)
    t.lt(90)

def STAIRS(n, length):
    pattern = ('l(length)')
    while n > 0:
        if pattern[-1] == l(length):
            #copy = pattern[::-1]
            #pattern.append(copy)
            pattern.add('r(length)')
        elif pattern[-1] == r(length):
            pattern.add('l(length')
        n -= 1
    t.fd(length)
    print(pattern)

# main program
t.pen(pencolor = "gold",
      fillcolor = "red",
      pensize = 3,
      speed = 1)

t.penup()
t.goto(-50, 0)
t.pendown()
STAIRS(20, 10)