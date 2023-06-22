def to_camel_case(name: str) -> str:
    result = ''
    for word in name.split("_"):
        result += word[0].upper() + word[1:]
    return result


print("Example:")
print(to_camel_case("my_function_name"))

# These "asserts" are used for self-checking
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")