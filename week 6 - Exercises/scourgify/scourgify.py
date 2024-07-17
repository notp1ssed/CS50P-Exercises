import sys, csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            clean_csv(sys.argv[1], sys.argv[2])
        else:
            sys.exit("Not a CSV file")



def clean_csv(arg1, arg2):
    try:
        with open(arg1) as file: # ler o csv
            reader = csv.DictReader(file) # esta funcao le dictionaires
            with open(arg2, "w") as file: # 'w' write
                header = ["first","last","house"]
                writer = csv.DictWriter(file, fieldnames = header)
                writer.writeheader()  # write header first
                for row in reader:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    writer.writerow(({"first": first, "last": last, "house": house}))
    except FileNotFoundError:
        sys.exit(f"Could not read {arg}")



if __name__ == "__main__":
    main()
