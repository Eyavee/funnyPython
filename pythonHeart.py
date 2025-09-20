#Python Heart

import turtle

#Инициализация окна и черепашки
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

#Установка цвета пера
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.fillcolor("red")

#Установка начальной позиции пера
pen.penup()
pen.goto(0, -100)
pen.pendown()

#Рисовка
pen.begin_fill()
pen.left(140)
pen.forward(180)


pen.circle(-90, 200)


pen.setheading(60)
pen.circle(-90, 200)


pen.forward(180)
pen.end_fill()

#Скрывание черепашки и завершение работы
pen.hideturtle()
turtle.done()