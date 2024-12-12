ok=1
A=set()
for a in range (1, 65):
   ok=1
   for x in range (0, 65):
      if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))) == 0:
         ok=0
   if ok:
      A.add(a)
      break
print(min(A))