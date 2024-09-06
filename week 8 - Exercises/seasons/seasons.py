from datetime import date
import inflect
import sys
import operator

p = inflect.engine()

def main():
    try:
        birth_date = date.fromisoformat(input("What's your birth day? YYYY-MM-DD:  "))
        delta = operator.sub(date.today(), birth_date)
        print(convert(delta.days))
    except ValueError:
        sys.exit("Invalid date")

def convert(days):
    minutes = days * 24 * 60
    phrase = p.number_to_words(minutes, andword='').capitalize()
    return f"{phrase} minutes"

if __name__ == "__main__":
    main()


