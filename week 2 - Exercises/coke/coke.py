def main():
    amount_due = 50
    while True:
        prompt = int(input("\nInsert Coin: "))
        if prompt == 25:
                amount_due = amount_due - prompt
        elif prompt == 10:
                amount_due -= prompt
        elif prompt == 5:
                amount_due -= prompt

        if amount_due > 0:
            print(f"\nAmount Due: {amount_due}")
        elif amount_due <= 0:
            #change_owed = amount_due * -1~
            change_owed = abs(amount_due)
            print(f"\nChange Owed: {change_owed}")
            break

main()
