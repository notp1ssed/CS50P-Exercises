def main():
    prompt = input("Input: ").strip()
    print((shorten(prompt)))

change = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def shorten(word):
    shorted = []
    for letter in word:
        if letter in change:
            pass # ignora as vogais
        else:
            shorted.append(letter) # qualquer coisa que nao seja vogal aproveita e junta a lista
    return str("".join(shorted)) # conversao de lista para string


if __name__ == "__main__":
    main()
