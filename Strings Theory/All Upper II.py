def is_all_upper(text):
    newstr = str(text).replace(' ', '')
    newstr = ''.join(''.join(i) for i in newstr if i.isalpha())
    if len(newstr) == 0 or newstr.isalpha() == False:
        return False
    else:
        return str(newstr).isupper()




print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == False
assert is_all_upper('123') == False
assert is_all_upper('DIGITS123') == True

print("The mission is done! Click 'Check Solution' to earn rewards!")