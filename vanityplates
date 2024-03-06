import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if s[0:2].isalpha():
        pass
    else:
        return False
    if 2 <= len(s) <= 6:
        pass
    else:
        return False
    if s.isalpha():
        return True
    for character in s:
        if character in string.punctuation:
            return False
    for character in s:
        if character.isdigit():
            break #using return will stop the continued execution of function
    if character == "0":
        return False
    if s[s.index(character): ].isdigit(): #checking if all characters after non-zero number are digits
        return True
    else:
        return False


main()

