import turtle

n = int(input('Podaj liczbę wierzchołków: '))
kat = 360 / n
bok = 1000 / n

t = turtle.Turtle()
for i in range(n):
    t.forward(bok)
    t.left(kat)

turtle.mainloop()


