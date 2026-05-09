from random import choice, random
from turtle import (
    begin_fill, clear, dot, down, done, end_fill, forward, goto,
    hideturtle, left, listen, onkey, ontimer, setup, tracer, up, update
)

from freegames import vector


def valor():
    """Genera un valor aleatorio entre (-5, -3) o (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])


pelota = vector(0, 0)
direccion = vector(valor(), valor())
estado = {1: 0, 2: 0}


def mover(jugador, cambio):
    """Mueve la posición del jugador según el cambio."""
    estado[jugador] += cambio


def rectangulo(x, y, ancho, alto):
    """Dibuja un rectángulo en (x, y) con el ancho y alto dados."""
    up()
    goto(x, y)
    down()
    begin_fill()
    for paso in range(2):
        forward(ancho)
        left(90)
        forward(alto)
        left(90)
    end_fill()


def dibujar():
    """Dibuja el juego y mueve la pelota de pong."""
    clear()
    rectangulo(-200, estado[1], 10, 100)  # Las paletas son el doble de largas.
    rectangulo(190, estado[2], 10, 100)

    pelota.move(direccion)
    x = pelota.x
    y = pelota.y

    up()
    goto(x, y)
    dot(10)
    update()

    if y < -200 or y > 200:
        direccion.y = -direccion.y

    if x < -185:
        inferior = estado[1]
        superior = estado[1] + 50

        if inferior <= y <= superior:
            direccion.x = -direccion.x
        else:
            return

    if x > 185:
        inferior = estado[2]
        superior = estado[2] + 50

        if inferior <= y <= superior:
            direccion.x = -direccion.x
        else:
            return

    ontimer(dibujar, 50)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: mover(1, 40), 'w')  # Las paletas son el doble de rapidas.
onkey(lambda: mover(1, -40), 's')
onkey(lambda: mover(2, 40), 'i')
onkey(lambda: mover(2, -40), 'k')
dibujar()
done()
