# made with love by hlnaji

import turtle

def draw_star(size, star_color):
    hlnaji = turtle.Turtle()
    hlnaji.shape("turtle")
    hlnaji.color(star_color)
    hlnaji.speed(1)
    hlnaji.width(9)
    hlnaji.goto(-150, 0)

    for _ in range(5):
        hlnaji.forward(size)
        hlnaji.right(180 * 4 / 5)

    hlnaji.ht()
    
def draw_outline(size, star_color):
    hlnaji = turtle.Turtle()
    hlnaji.shape("turtle")
    hlnaji.color(star_color)
    hlnaji.speed(1)
    hlnaji.width(12)
    hlnaji.goto(-150, 0)

    for _ in range(5):
        hlnaji.forward(size)
        hlnaji.right(180 * 4 / 5)

    hlnaji.ht()



window = turtle.Screen()
window.bgcolor((193/255, 39/255, 45/255))
draw_outline(250, (1/255, 1/255, 1/255))
draw_star(250, (0/255, 98/255, 51/255))


window.exitonclick()