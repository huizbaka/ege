import turtle as tr

wn = tr .Screen()

wn.tracer(0)

tr.speed(100)

step = 30

for i in range(4):
    tr.forward(12 * step)
    tr.right(90)
for i in range(5):
    tr.forward(4 * step)
    tr.right(45)

tr.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        tr.goto(x * step, y * step)
        tr.dot()
wn.update()
wn.mainloop()