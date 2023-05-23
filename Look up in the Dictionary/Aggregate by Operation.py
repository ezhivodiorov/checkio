def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    result = {}
    final = {}
    for item in data:
        sign = item[0][0]
        key = item[0][1]
        number = item[1]
        currentnumber = 0 if result.get(key) == None else result.get(key)
        if sign == '+':
            result[key] = currentnumber + number
        elif sign == '-':
            result[key] = currentnumber - number
        elif sign == '*':
            result[key] = currentnumber * number
        else:
            if number != 0:
                result[key] = currentnumber / number

        for item in result.items():
            if item[1] !=0:
                final[item[0]] = item[1]
    return final


print("Example:")
print(aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]))

# These "asserts" are used for self-checking
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")