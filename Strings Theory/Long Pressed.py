def compress(text: str):
    newtext = []
    prev = None
    for i in text:
        if i != prev:
            newtext.append(i)
            prev = i

    # return ''.join((newtext.append(i), prev) for i in text if i != prev)
    return ''.join(newtext)

def long_pressed(text: str, typed: str) -> bool:
    return compress(text) == compress(typed)


print("Example:")
assert long_pressed('welcome boss!', 'welcooome bos!!') == False
print(long_pressed("alex", "aaleex"))

# These "asserts" are used for self-checking
assert long_pressed("alex", "aaleex") == True
assert long_pressed("welcome to checkio", "weeeelcome to cccheckio") == True
assert long_pressed("there is an error here", "there is an errorrr hereaa") == False
assert long_pressed("hi, my name is...", "hi, my name is...") == False


print("The mission is done! Click 'Check Solution' to earn rewards!")