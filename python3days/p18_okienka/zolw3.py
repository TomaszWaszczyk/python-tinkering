import turtle

# TODO: napisz program, który wczytuje od użytkownika liczbę całkowitą i rysuje wielokąt foremny o tylu wierzchołkach

# n = int(input('Podaj liczbę wierzchołków:'))
n = int(turtle.numinput('Pytanie', 'Podaj liczbę wierzchołków:'))

zolw = turtle.Turtle()

zolw.speed(100)
zolw.color('red', 'yellow')
zolw.width(5)

obwod = 1200
kat = 360 / n
bok = obwod / n

zolw.penup()
zolw.goto(-bok/2, -obwod/6.5)
zolw.pendown()

zolw.begin_fill()
for i in range(n):
    zolw.forward(bok)
    zolw.left(kat)
zolw.end_fill()

turtle.mainloop()

# ewentualnie obsługa zdarzeń i dalsze działania...



