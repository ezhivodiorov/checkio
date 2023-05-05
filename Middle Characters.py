def middle(text: str) -> str:
    return text[len(text)//2] if len(text) % 2 != 0 else text[int(len(text)/2)-1] + text[int(len(text)/2)]

print("Example:")
print(middle("test"))

# # These "asserts" are used for self-checking
# assert middle("example") == "m"
# assert middle("test") == "es"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")