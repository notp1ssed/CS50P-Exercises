def main():
    total()

prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def total():
    amount_due = 0
    while True:
        try:
            x = input("Item: ").title()
            if x in prices:
                amount_due = amount_due + float(prices[x])
                print(f"Total: ${amount_due:.2f}")
            else:
                pass
        except ValueError:
            pass
        except EOFError:  # quando o user faz Ctrl + D
            break
main()
