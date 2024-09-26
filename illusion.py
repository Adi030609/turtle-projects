import turtle

screen = turtle.Screen()
screen.title("Café Wall Illusion")
screen.setup(width=1.0, height=1.0)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

def draw_rectangle(x, y, width, height, color):
    t.goto(x, y)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

rows = 10
cols = 10
block_width = 50
block_height = 30
shift = block_width // 2

for row in range(rows):
    y = row * block_height * -1 + 200
    x_shift = (row % 2) * shift
    for col in range(cols):
        x = col * block_width * 2 - (cols * block_width * 2) / 2 + x_shift
        draw_rectangle(x, y, block_width, block_height, "black")

t.pensize(2)
t.color("black")
for row in range(rows + 1):
    y = row * block_height * -1 + 200
    t.penup()
    t.goto(-block_width * cols, y)
    t.pendown()
    t.forward(block_width * cols * 2)

turtle.done()