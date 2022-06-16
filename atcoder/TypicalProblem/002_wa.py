class Parentheses:
    def __init__(self, is_open: bool):
        self.is_open = is_open

    def txt(self) -> str:
        return "(" if self.is_open else ")"

    def reverse(self):
        return Parentheses(not self.is_open)

    def __str__(self):
        return self.txt()


N = int(input())
n = 2 ** (N // 2) + 1
G = []
for i in range(n):
    G.append(-1)

if N % 2 == 0:
    G[0] = Parentheses(True)
    for i in range(1, n):
        p = (i - 1) // 2
        if i == p * 2 + 1:
            G[i] = Parentheses(True)
        else:
            G[i] = Parentheses(False)
    if N == 2:
        leaves = [0]
    else:
        leaves = list(range((2 ** (N//2 - 1)-1), (2 ** (N//2)) - 1))
    # print(leaves, list(map(str, G)))
    for index in leaves:
        # print("index", index)
        j = index
        if G[index] == -1:
            continue
        ans = "("
        groups = []
        while j > 0:
            # print("j", j)
            groups.append(G[j])
            parent = (j-1) // 2
            j = parent
        r = reversed(list(map(lambda p: p.reverse().txt(), groups)))
        groups = list(map(lambda p: p.txt(), groups))
        ans += "".join(groups) + "".join(r)
        ans += ")"
        print(ans)
