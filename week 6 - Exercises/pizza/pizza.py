import sys, csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            read_csv(sys.argv[1])
            print(tabulate(prices, headers="keys", tablefmt="grid"))
        else:
            sys.exit("Not a CSV file")

prices = []

def read_csv(arg):
    try:
        with open(arg) as file:
            reader = csv.DictReader(file) # esta funcao le dictionaires
            for row in reader:
                if sys.argv[1] == "regular.csv":
                    prices.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
                elif sys.argv[1] == "sicilian.csv":
                    prices.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})
            return prices
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
