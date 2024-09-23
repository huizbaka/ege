import turtle as t

dist = 70
t.speed(100)

for step in range(12):
    t.right(60)
    t.forward(dist)
    t.right(60)
    t.forward(dist)
    t.right(270)
t.penup()

t.speed(400)

for x_coord in range(-10, 10):
    for y_coord in range(-10, 10):
        t.setpos(x_coord * dist, y_coord * dist)
        t.dot(5)

t.done()
