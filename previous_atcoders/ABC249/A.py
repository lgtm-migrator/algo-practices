A, B, C, D, E, F, X = map(int, input().split())


def calc(t, speed, break_time) -> int:
    cycle = X // (t + break_time)
    remain = X % (t + break_time)
    distance = cycle * t * speed
    if remain >= t:
        distance += t * speed
    else:
        distance += remain * speed
    return distance


t = calc(A, B, C)
a = calc(D, E, F)
if t > a:
    print("Takahashi")
elif t < a:
    print("Aoki")
else:
    print("Draw")
