from typing import Union

def sun_angle(time: str) -> Union[float, str]:
    h, m  = map(int, time.split(":"))
    angle = h*15 + m*0.25 - 90
    return angle if angle >= 0 and angle <= 180 else "I don't see the sun!"


print("Example:")
print(sun_angle("05:55"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75
assert sun_angle('18:00') == 180
assert sun_angle('18:00') == 180
assert sun_angle('05:55') == "I don't see the sun!"

print("The mission is done! Click 'Check Solution' to earn rewards!")