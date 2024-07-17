def main():
    name = input("\ncamelCase: ")
    convert(name)

def convert(a):
    for letter in a:
        if letter.islower():
            print(letter, end = "")
        elif letter.isupper():
            letter = letter.lower()
            print("_", letter, sep = "", end = "")

main()
