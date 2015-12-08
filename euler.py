def function(x, t):
    return x


def arange(start, stop, step):
    """since range only accepts integers
    we must use our own function"""
    r = start
    while r <= stop:
        yield r
        r += step


def main():
    x = float(input("Podaj x0: "))
    eps = float(input("Podaj dokladnosc: "))

    h = 1  # step
    points = [(0,x)]

    for i in arange(h, 4, h):
        x = x + h * function(x,i)
        points.append((i,x))

    print(points)

if __name__ == '__main__':
    main()
