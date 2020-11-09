# klasa: Turtle
# obiekty: czerwony, zielony
from turtle import Turtle, mainloop

czerwony = Turtle()
czerwony.color('red')
czerwony.width(5)

zielony = Turtle()
zielony.color('green')
zielony.width(5)

czerwony.forward(200)
czerwony.left(90)
czerwony.forward(200)
zielony.penup()
zielony.goto(-300, -300)
zielony.pendown()
zielony.left(45)
zielony.forward(10)

# wpisanie obiektu na zmienną nie towrzy nowego obiektu, tylko odnosi się do istniejącego
x = zielony
x.forward(300)
zielony.left(135)
x.backward(50)

x = czerwony
x.left(90)
x.forward(200)

for z in (zielony, czerwony, zielony, zielony, czerwony):
    z.forward(50)
    z.left(120)

mainloop()
