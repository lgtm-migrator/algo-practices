S = list(map(str, input()))
has_upper = False
has_lower = False
is_differential = True
kinds = set()
for s in S:
    if s.isupper():
        has_upper = True
    if s.islower():
        has_lower = True
    if s in kinds:
        is_differential = False
    kinds.add(s)

print("Yes" if has_upper and has_lower and is_differential else "No")
