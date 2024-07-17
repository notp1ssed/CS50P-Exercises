import validators

def main():
    print(check(input("What's your email address? ")))


def check(string):
    if validators.email(string) == True:
        return f"Valid"
    else:
        return f"Invalid"


if __name__ == "__main__":
    main()
