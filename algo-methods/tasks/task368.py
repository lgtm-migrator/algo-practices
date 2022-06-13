N = float(input())

r = 100
l = 0


def f(x: float) -> float:
    return x * (x * (x + 1) + 2) + 3


while r - l >= 10 ** -4:
    mid = (r + l) / 2
    l_eq = f(l)
    r_eq = f(r)
    mid_eq = f(mid)
    if mid_eq < N:
        l = mid
    elif mid_eq > N:
        r = mid
    else:
        break

print(r)
