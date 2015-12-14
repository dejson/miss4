import matplotlib.pyplot as plt
import numpy


M=1.0
L=1.0


def function(x, t):
    return numpy.cos(x*t*1000)


def arange(start, stop, step):
    """since range only accepts integers
    we must use our own function"""
    r = start
    while r <= stop:
        yield r
        r += step


def GTE(h):
    """Calculate global truncation error"""
    return h*M/(2*L) * (numpy.e**L - 1)


def calculate_step(h, eps):
    if GTE(h) < eps:
        return h

    return calculate_step(h/2, eps)


def main():
    x = float(input("Podaj x0: "))
    eps = float(input("Podaj dokladnosc: "))

    h = calculate_step(1.0, eps)  # step
    print("Krok: %f" % h)
    points = [(0,x)]

    for i in arange(h, 1, h):
        x = x + h * function(x,i)
        points.append((i,x))

    points = map(list, zip(*points))
    plt.plot(points[0], points[1])
    plt.show()

if __name__ == '__main__':
    main()
