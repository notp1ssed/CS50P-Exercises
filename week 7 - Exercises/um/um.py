import re
import sys


def main():
    print(count(input("Text: ")))

def count(string):
    matches = re.findall(r"(^|\W)um($|\W)", string, re.IGNORECASE)
    if matches:
        return(len(matches))


if __name__ == "__main__":
    main()
