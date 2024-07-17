months ={
    "January":"1",
    "February":"2",
    "March":"3",
    "April":"4",
    "May":"5",
    "June":"6",
    "July":"7",
    "August":"8",
    "September":"9",
    "October":"10",
    "November":"11",
    "December":"12"}


def main():
    while True:
        x = input("Date: ").strip()
        try:
            if x[0].isdigit():
                mm, dd, yyyy = x.split(sep="/")
            elif x[0].isalpha():
                mmdd, yyyy = x.split(sep=",")
                mm, dd = mmdd.split(sep=" ")
                mm = mm.title()
                mm = months[mm]
            else:
                raise ValueError

            if int(mm) > 12 or int(dd) > 31:
                raise ValueError

        except ValueError:
            pass
        else:
            print (f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
            break


main()
