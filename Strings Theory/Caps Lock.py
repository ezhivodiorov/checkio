def caps_lock(text: str) -> str:
    uppLock = False
    new_text = ''

    for i in text:
        if i.isupper():
            new_text +=i
        elif i.lower() == 'a':
            uppLock = not uppLock
        else:
            new_text += i.upper() if uppLock else i.lower()

    return new_text


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")