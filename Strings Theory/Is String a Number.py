def is_number(val: str) -> bool:
    return str.isdigit()


print("Example:")
print(is_number("10"))

# These "asserts" are used for self-checking
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
