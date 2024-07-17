def main():
    ask = input("What time is it? ").strip()
    result = convert(ask)
    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")
    else:
        return None

def convert(time):
    hours, minutes = time.split(":") # separa nos :
    fhours = float(hours)
    fminutes = float(minutes) / 60
    return (fhours + fminutes)

if __name__ == "__main__":
    main()
