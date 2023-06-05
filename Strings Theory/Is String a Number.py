def is_number(val: str) -> bool:
    result = True
    arifmetic = '-+/*'
    result = len(val) != 0
    wasNubmer = False
    for i in val:
        if i.isalpha():
            result = False
            break
        elif i.isnumeric():
            wasNubmer = True
        elif (i in arifmetic) and wasNubmer:
            result = False
            break

    return result if wasNubmer else False


print("Example:")
print(is_number("--5"))

# These "asserts" are used for self-checking
assert is_number("--5") == False
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("+10.05") == True
assert is_number("1OOO") == False
assert is_number("1.") == True
assert is_number("+.l") == False
assert is_number("++1+.2-") == False
assert is_number("3e4") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
