def main():
    fraction = input("Fraction: ")
    pct = convert(fraction)
    print(gauge(pct))

def convert(fraction):
        x, y = fraction.split(sep="/")        # assign de cada variavel a uma posicao
        if int(x)/int(y) > 1:  # caso x seja maior que y
            raise ValueError
        elif int(y) == 0:
            raise ZeroDivisionError
        return int(int(x) / int(y) *100)

def gauge(percentage):
    try:
        if 0 <= percentage <= 1:
            return "E"
        elif 99 <= percentage <= 100:
            return "F"
        elif 1 < percentage < 99:
            return f"{int(percentage)}%"
        else:
            raise TypeError
    except TypeError:
        pass

if __name__ == "__main__":
    main()
