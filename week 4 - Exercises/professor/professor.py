import random

def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if 1 <= x <= 3:
                return x
        except ValueError:
            pass


def generate_integer(level):
    correct = 0
    nr = 0
    while True:
        try:
            if nr < 10:
                    nr += 1
                    wrong = 0
                    if level == 1:
                        x = random.randint( 0 , 9 )
                        y = random.randint( 0 , 9 )
                        while True:
                            if wrong != 3:
                                answer = int(input(f" {x} + {y} = "))
                                if ( answer - ( x + y)) == 0:
                                    correct += 1
                                    break # caso a pergunta esteja correta sai do loop das 3 respostas erradas
                                elif wrong != 3:
                                    print("EEE")
                                    wrong += 1
                            elif wrong == 3:
                                print(f"{x}+{y}={x + y}")
                                break # break do loop das 3 erradas
                    elif level == 2:
                        x = random.randint( 10 , 99 )
                        y = random.randint( 10 , 99 )
                        while True:
                            if wrong != 3:
                                answer = int(input(f" {x} + {y} = "))
                                if ( answer - ( x + y)) == 0:
                                    correct += 1
                                    break # caso a pergunta esteja correta sai do loop das 3 respostas erradas
                                elif wrong != 3:
                                    print("EEE")
                                    wrong += 1
                            elif wrong == 3:
                                print(f"{x}+{y}={x + y}")
                                break # break do loop das 3 erradas
                    elif level == 3:
                        x = random.randint( 100 , 999 )
                        y = random.randint( 100 , 999 )
                        while True:
                            if wrong != 3:
                                answer = int(input(f" {x} + {y} = "))
                                if ( answer - ( x + y)) == 0:
                                    correct += 1
                                    break # caso a pergunta esteja correta sai do loop das 3 respostas erradas
                                elif wrong != 3:
                                    print("EEE")
                                    wrong += 1
                            elif wrong == 3:
                                print(f"{x}+{y}={x + y}")
                                break # break do loop das 3 erradas
                    else:
                        pass
            elif nr == 10:      # nas 10 perguntas dá o score
                print(f"Score: {correct}")
                break
        except ValueError:
            pass
        except EOFError:    # quando o user faz Ctrl + D
            break

if __name__ == "__main__":
    main()

