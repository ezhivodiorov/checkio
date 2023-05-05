from collections import Counter

def checkio(text: str) -> str:
    dict = {}
    for letter in text:
        if letter.isalpha():
            dict[letter.lower()] = dict.get(letter.lower(), 0) + 1
    maxcount = max(dict.values())
    most_frequent_letters = sorted([letter for letter, count in dict.items() if count == maxcount])
    return most_frequent_letters[0]


print("Example:")
print(checkio("Hello World!"))

# These "asserts" are used for self-checking
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")
