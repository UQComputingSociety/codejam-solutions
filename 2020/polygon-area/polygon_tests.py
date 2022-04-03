import sys 
import random 
import math as m

def irregular_polygon(N=None):
    N = N or random.randint(3, 100000)
    s = abs(random.normalvariate(100, 100))
    s = 1e50
    centre = [random.uniform(-s, s) for _ in range(2)]
    centre = [0,0]

    angles = [random.random() for i in range(N)]
    s = sum(angles)
    angles = [ i/s * 2*m.pi for i in angles ]

    a = random.random() * 2 * m.pi
    print(N)
    ma = max(centre)
    for n in range(N):
        r = abs(random.uniform(0.9, 1) * s)
        x = m.cos(a) * r 
        y = m.sin(a) * r 
        x = round(x)
        y = round(y)
        print(x + centre[0], y + centre[1], sep=' ')
        a += angles[n]

def square(side=1):
    N = 4 * side
    dx, dy = 1, 0
    x, y = 0, 0
    print(N)
    for i in range(N):
        print(x,y)
        x, y = x+dx, y+dy
        if (i+1) % side == 0:
            dx, dy = -dy, dx



if __name__ == "__main__":
    arg = int(sys.argv[1]) if len(sys.argv) > 1 else None
    square(arg)