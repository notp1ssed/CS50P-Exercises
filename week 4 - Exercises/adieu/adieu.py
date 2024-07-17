# pip install inflect

import inflect
p = inflect.engine()


def main():
    stored_names = [] # empty list
    while True:
        try:
            x = input("Name: ")
            stored_names.append(x)
        except EOFError:    # quando o user faz Ctrl + D
            print(f"\nAdieu, adieu, to {p.join((stored_names))}")
            break

main()
