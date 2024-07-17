def main():
    greeting = input("\nWhat's you greeting? ").lower().strip()
    if hello_func(greeting):
        print("$0")
    elif h_func(greeting):
        print("$20")
    else:
        print("$100")

def hello_func(txt):
    if txt.startswith("hello"):
        return True
    else:
        return False

def h_func(txt):
    return txt.startswith("h") # simpler version to achieve True or False

main()
