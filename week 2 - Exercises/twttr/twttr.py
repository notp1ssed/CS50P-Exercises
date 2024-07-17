def main():
    prompt = input("Input: ").strip()
    convert(prompt)

change=["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def convert(x):
    for letter in x:
        if letter not in change:
            print(letter, end="")
        elif letter in change:
            print("", end="")

main()
