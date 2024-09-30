import turtle as turtle_lib

turtle_lib.speed(100)
scale = 10

for step in range(6):
    turtle_lib.forward(10 * scale)
    turtle_lib.right(60)

turtle_lib.penup()
turtle_lib.speed(10000)

for x_val in range(-5, 20):
    for y_val in range(-20, 10):
        turtle_lib.goto(x_val * scale, y_val * scale)
        turtle_lib.dot(5)
turtle_lib.done()
