
def translate(text: str) -> str:
    letters = 'aeiouy'
    newtext = ''
    propustit = False
    letter = ''

    for i in text:
        if propustit and i in letters:
            propustit = False
            continue
        elif i not in letters and i.isalpha():
            letter = i
            propustit = True
        elif letter == i:
            continue
        else:
            letter = i

        newtext += letter
    return newtext


print("Example:")
print(translate("sooooso aaaaaaaaa"))

# # These "asserts" are used for self-checking
# assert translate("hieeelalaooo") == "hello"
# assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
# assert translate("aaa bo cy da eee fe") == "a b c d e f"
# assert translate("sooooso aaaaaaaaa") == "sos aaa"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")