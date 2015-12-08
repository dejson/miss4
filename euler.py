def function(x, t):
    return x*t
    
def main():
    x0 = float(input("Podaj x0: "))
    eps = float(input("Podaj dokladnosc: "))
    
    print(function(x0, eps))
    
if __name__ == '__main__':
    main()