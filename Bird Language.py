
def translate(text: str) -> str:
    signt = 'aeiouy'
    newtext = ''
    lenght = len(text) -1
    count = 0
    while count < lenght:
        letter = text[count]
        if letter.isalpha():
            if letter in signt:
                count += 3
            else:
                count += 2
        else:
            count += 1
        newtext += letter

    return newtext


print("Example:")
print(translate("sooooso aaaaaaaaa"))

# These "asserts" are used for self-checking
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")