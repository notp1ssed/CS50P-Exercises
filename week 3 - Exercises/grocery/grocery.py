def main():
    construcao()

def construcao():
    lista_completa = {} # empty dictionary
    while True:
        try:
            key = input().upper().strip()
            if key in lista_completa:
                lista_completa[key] += 1   # caso o valor ja esteja na lista, adiciona +1 à contagem
            elif key not in lista_completa:
                lista_completa[key] = int(1)
        except KeyError:    # when a mapping (dictionary) key is not found in the set of existing keys.
            pass
        except EOFError:  # quando o user faz Ctrl + D
            for i in sorted(lista_completa):
                print(lista_completa[i], i)     # value da key 'i', key 'i'
            break


main()
