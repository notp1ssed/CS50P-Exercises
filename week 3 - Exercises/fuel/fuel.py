def main():
    a = get_fraction("Fraction: ")
    if a >= 0.99:
        print("F")
    elif a <= 0.01:
        print("E")
    else:
        print(f"{a:.0%}")


def get_fraction(prompt):
    while True:
        try:
            x = input(prompt).strip()
            x = x.split(sep="/")        # torna-se em uma lista
            if int(x[0]) <= int(x[1]):  # aqui para comparar, tenho que comparar já em int(), caso contrario compara em str()
                return ( int(x[0]) / int(x[1]) )
        except ValueError:
            pass        # keep looping
        except ZeroDivisionError:
            pass        # keep looping


main()
