import sys

count = 0

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".py"):
            print(count_lines(sys.argv[1]))
        else:
            sys.exit("Not a Python file")


def count_lines(arg):
    try:
        count = 0
        with open(arg) as file:
            for row in file:
                if not (row.lstrip().startswith("#") or row.strip() == ""): # se a linha começar com ( # ) ignora, se a linha estiver vazia ( "" ) ignora. Conta apenas as restantes
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
