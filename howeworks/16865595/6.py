import turtle as tr

step = 1

wn = tr.Screen()

wn.tracer(0)

for i in range(2):
    tr.forward(24 * step)
    tr.right(90)
    tr.forward(10 * step)
    tr.right(90)

tr.forward(3 * step)
tr.left(90)
tr.forward(13 * step)
tr.right(90)

for i in range(2):
    tr.forward(9 * step)
    tr.right(90)
    tr.forward(32 * step)
    tr.right(90)

tr.up()

for x in range(0 * step, 40 * step, step):
    for y in range(-30 * step, 20 * step, step):
        tr.goto(x, y)
        tr.dot(3, "red")

wn.update()

tr.done()