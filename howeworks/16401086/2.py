print("x,y,z,w")

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (((x or not(y)) and (not(z) == w)) <= (y and z))
                if not(F):
                    print(x, y, z, w)
