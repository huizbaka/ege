import turtle as turtle_lib

turtle_lib.speed(100)
scale_factor = 10

for step in range(3):
    turtle_lib.forward(7 * scale_factor)
    turtle_lib.right(90)

turtle_lib.forward(8 * scale_factor)

for step in range(3):
    turtle_lib.left(90)
    turtle_lib.forward(5 * scale_factor)

turtle_lib.penup()

for x_val in range(-10, 10):
    for y_val in range(-10, 10):
        turtle_lib.goto(x_val * scale_factor, y_val * scale_factor)
        turtle_lib.dot(3)
turtle_lib.done()
