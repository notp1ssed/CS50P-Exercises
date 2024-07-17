def main():
    greeting = input("\nWhat's you greeting? ").strip()
    print(f"${value(greeting)}")

def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

'''
anteriormente tinha o lower() no input, porém
para testes, fica melhor na funcao do check
'''
