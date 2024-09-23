print("x,y,z,w")

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = ((y or z) <= (z and w)) == (not(x and z) <= (w or y))
                if F:
                    print(x, y, z, w)