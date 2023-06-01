from typing import Union

def sun_angle(time: str) -> Union[float, str]:
    h, m  = map(int, time.split(":"))
    angle = h*15 + m*0.25 - 90
    return "I don't see the sun!" if angle <= 0 or angle >= 180 else angle


print("Example:")
print(sun_angle("18:01"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75
assert sun_angle('18:00') == 180

print("The mission is done! Click 'Check Solution' to earn rewards!")