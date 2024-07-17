def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum(): #alnum -> letters or numbers
        if s.isalpha():  # Return true if characters are all letters, in case of only letters plates
            return True
        else:
            if s[:2].isalpha() and s[-2:].isdigit():
                for i in range(len(s)):
                    if s[i].isdigit():
                        if s[i].startswith("0") or s[i:].isalpha():  # Return false if number starts with 0 or the following character is letter
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False



main()
