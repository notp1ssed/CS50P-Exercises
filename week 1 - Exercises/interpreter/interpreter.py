def main():
    expression = input("Expression: ")
    x, y, z = expression.split()
    result = calculator(x, y, z)
    print(f"{result:.1f}")


def calculator(x, y, z):
    fx = float(x)
    fz = float(z)
    if y == "+":
        return fx + fz
    elif y == "-":
        return fx - fz
    elif y == "*":
        return fx * fz
    elif y == "/":
        if fz != 0:
            return fx / fz
        else:
            print("Error: Can't divide by zero!")
            return None # Return None to indicate an error
    else:
        print("Error: Arithmetic Operation Error!")
        return None # Return None to indicate an error

main()
