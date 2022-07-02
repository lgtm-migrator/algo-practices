N, Q = map(int, input().split())

messages = list(map(str, input()))

queries = []

index = 0

for i in range(Q):
    ope, x = map(int, input().split())
    queries.append((ope, x))


def ope1(x: int):
    global index
    index -= x


def ope2(x: int):
    global messages
    i = (index + x) % len(messages)
    print(messages[i])


for query in queries:
    ope, x = query
    if ope == 1:
        ope1(x)
    elif ope == 2:
        x -= 1
        ope2(x)
