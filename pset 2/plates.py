def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s.isalnum():
        return False
    if not s[:2].isalpha():
        return False

    found_number = False
    for n in range(2, len(s)):
        if s[n].isdigit():
            if not found_number:
                if s[n] == "0":
                    return False
                found_number = True
        else:
            if found_number:
                return False

    return True

main()
