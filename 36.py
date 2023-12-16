a = 36
b = 30
c = 0
d = -2
e = -7

def approve(x, y, z, z2, z3):
    while x**2 > y**2 + z**2:
        x += 1
        y += 1
        z += 1
    print(x, y, z)

approve(a, b, c, d, e)
