import math
piq6 = 0
for i in range(1, 10000000):
    r = 1.0 / (i*i)
    piq6 += r
    #pi = math.sqrt(piq6 * 6)
    #print(i, r, piq6, pi)

pi = math.sqrt(piq6 * 6)
print(pi)
