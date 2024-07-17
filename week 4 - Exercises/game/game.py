import random

while True: # definir o n
    try:
        n = int(input("Level: "))
        if int(n) > 0:
            random_int = random.randint( 1 , n )
        while True: # caso o n seja int() positivo ativa este loop
            x = int(input("Guess: "))
            if x < random_int:
                print("Too small!")
            elif x > random_int:
                print("Too large!")
            elif x == random_int:
                print("Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:    # quando o user faz Ctrl + D
        break
