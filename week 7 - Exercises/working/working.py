import re

def main():
    print(convert(input("Hours: ")))

def hours_converter(in_hour, in_minutes, period):
    if period == "AM":
        if in_hour != "12":
            hours = f"{int(in_hour):02}"
        else:
            hours = "00"

    elif period == "PM":
        if in_hour != "12":
            hours = f"{int(in_hour)+12:02}"
        else:
            hours = "12"
    if in_minutes is None:
        minutes = "00"
    else:
        minutes = f"{int(in_minutes):02}"

    return f"{hours}:{minutes}"


def convert(string):
    regex = "(0?[1-9]|1[0-2]):?[.]?([0-5][0-9])? (AM|PM)"
    matches = re.search(r"^" + regex + " to " + regex + "$", string)
    if matches:
        from_hour = hours_converter(matches.group(1), matches.group(2), matches.group(3))
        to_hour = hours_converter(matches.group(4), matches.group(5), matches.group(6))
        return f"{from_hour} to {to_hour}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
