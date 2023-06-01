from typing import Union

def sun_angle(time: str) -> Union[float, str]:
    h, m  = map(int, time.split(":"))
    return "I don't see the sun!" if h <= 6 or h >= 18 else h*15 + m*0.25 - 90


print("Example:")
print(sun_angle("18:01"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

print("The mission is done! Click 'Check Solution' to earn rewards!")