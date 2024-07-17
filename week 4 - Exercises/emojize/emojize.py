'''
# Inicialmente eu ia contruir o dicionario, mas são muitos valores... então lembrei-me que posso usar diretamente a biblioteca emoji
# dicionario dos codigos com os valores emoji guardados
dictionary = {
    ":thumbsup:":"👍"
}

def emojize(n):
    print(dictionary[n])
'''

# pip install emoji

import emoji

def main():
    x = input("Input: ").strip().lower()
    print(emoji.emojize(f"Output: {x}", language="alias"))



main()
