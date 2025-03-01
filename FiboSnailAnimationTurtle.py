import numpy as np
import math as re
import matplotlib.pyplot as plt
import turtle as t
t.screensize(1000, 1000)
t.pensize(3)
x = int(input("Enter the number of Fibonacci numbers you want to generate: "))

Fib_list = [0,1]
def main():
    Fibo1 =  0
    #Fib_list[1] = Fibo1
    Fibo2 = 1
    #Fib_list[2] = Fibo2
    Fib03 = 1
    for i in range(x):
        t.right(90)
        drawSquar(Fib03*10)
        Fib03 = Fibo1 + Fibo2
        Fibo1 = Fibo2
        Fibo2 = Fib03
        Fib_list.append(Fib03)
        print(Fib_list)
def drawSquar(side):
    for i in range(6):
        t.forward(side)
        t.left(90)
        t.speed(3)
def Spiral():
    t.penup()
    t.home()
    t.pendown()
    angle = 90
    t.speed(1)
    rr = 1.5
    r = rr
    for i in range(x):
        t.right(angle)
        t.circle(2*re.pi*Fib_list[i+1]*r, 90, steps=None)
        if angle == 0:
            angle = 0
        else:
            angle = angle - 90
        
        if i > 3:
            r = rr*1.05
        elif i > 4:
            r = rr*1.03
        elif i > 5:
            r = rr*1.02
        else:
            r = rr


main()
Spiral()
