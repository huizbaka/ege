print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not (x <= (z <= w) and (z <= (y == (not(w))))):
                    print(x, y, z, w)

# ВКИЖЕАГБД zxwy 472 00110