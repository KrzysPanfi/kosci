import turtle
t=turtle.Pen()
t.pencolor("red")
liczba_okrogow=int(turtle.numinput("Ilosc okregow", "Podaj ilosc okregow",6))
for x in range(liczba_okrogow):
    t.circle(100)
    t.left(360/liczba_okrogow)
