FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"

def conpnumber(num: int) ->set:
    setnumber = [0, 0, 0]
    numstr = str(num)
    if len(numstr) > 2:
        setnumber[0] = int(numstr[0])
        numstr = numstr[1:]
    if len(numstr) > 1:
        if int(numstr) == 10:
            setnumber[1] = int[0]
            numstr = ''
        elif int(numstr) < 20 and int(numstr) > 10:
            setnumber[1] = int(numstr)
            numstr = ''
        else:
            setnumber[1] = int(numstr[0])
            numstr = ''
    if len(numstr) > 0:
        setnumber[2] = int(numstr)

    return setnumber

def checkio(num: int) -> str:
    result =""
    setnumber = conpnumber(num)
    hubdr = setnumber[0]
    dec = setnumber[1]
    item = setnumber[2]
    if hubdr != 0:
        result = FIRST_TEN[hubdr] + ' ' + HUNDRED
    if dec != 0:
        if dec > 10:
            result = result + " " + SECOND_TEN[int(str(dec)[1])]
        else:
            result = result + " " + OTHER_TENS[dec]
    if item != 0:
        result = result + " " + FIRST_TEN[item]

    return result.lstrip()

conpnumber(152)

print("Example:")
print(checkio(312))
print(checkio(11))
print(checkio(12))
print(checkio(21))
print(checkio(4))

# These "asserts" are used for self-checking
assert checkio(1) == "one"
assert checkio(2) == "two"
assert checkio(3) == "three"
assert checkio(4) == "four"
assert checkio(5) == "five"
assert checkio(6) == "six"
assert checkio(9) == "nine"
assert checkio(10) == "ten"
assert checkio(11) == "eleven"
assert checkio(12) == "twelve"
assert checkio(13) == "thirteen"
assert checkio(14) == "fourteen"
assert checkio(15) == "fifteen"
assert checkio(16) == "sixteen"
assert checkio(17) == "seventeen"
assert checkio(18) == "eighteen"
assert checkio(19) == "nineteen"
assert checkio(999) == "nine hundred ninety nine"
assert checkio(784) == "seven hundred eighty four"
assert checkio(777) == "seven hundred seventy seven"
assert checkio(88) == "eighty eight"
assert checkio(44) == "forty four"
assert checkio(20) == "twenty"
assert checkio(30) == "thirty"
assert checkio(40) == "forty"
assert checkio(50) == "fifty"
assert checkio(80) == "eighty"
assert checkio(90) == "ninety"
assert checkio(100) == "one hundred"
assert checkio(200) == "two hundred"
assert checkio(300) == "three hundred"
assert checkio(600) == "six hundred"
assert checkio(700) == "seven hundred"
assert checkio(900) == "nine hundred"
assert checkio(21) == "twenty one"
assert checkio(312) == "three hundred twelve"
assert checkio(302) == "three hundred two"
assert checkio(509) == "five hundred nine"
assert checkio(753) == "seven hundred fifty three"
assert checkio(940) == "nine hundred forty"
assert checkio(999) == "nine hundred ninety nine"

print("The mission is done! Click 'Check Solution' to earn rewards!")
