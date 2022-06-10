from heapq import heappop, heappush, heapify


# binaryのTrie木
class BinaryTrie:

    def __init__(self, bit_depth):
        # [0-child, 1-child, count]
        self.root = [None, None, 0]
        # 2^(n-1)
        self.bit_start = 1 << (bit_depth - 1)
        self.bit_depth = bit_depth
        self.xor_mask = 0

    def add(self, x: int):
        b = self.bit_start
        node = self.root
        node[2] += 1
        while b:
            i = bool(x & b)
            if node[i] is None:
                node[i] = [None, None, 1]
            else:
                node[i][2] += 1
            node = node[i]
            b >>= 1

    def pop_min(self):
        """
        xor_maskを適用後の最小値を適用前の値で取得し、木からは削除
        """
        b = self.bit_start
        node = self.root
        m = self.xor_mask
        ret = 0
        node[2] -= 1
        while b:
            i = bool(m & b)
            if node[i] is None:
                i ^= 1
            ret = (ret << 1) + i

            if node[i][2] > 1:
                node[i][2] -= 1
                node = node[i]
            else:
                tmp = node[i]
                node[i] = None
                node = tmp
            b >>= 1
        return ret

    def get_min(x: int):
        """
        xor_maskを適用後の最小値を取得
        """
        b = self.bit_start
        node = self.root
        m = self.xor_mask
        ret = 0
        while b:
            i = bool(m & b)
            ret = ret << 1
            if node[i] is None:
                i ^= 1
                ret += 1
            node = node[i]
            b >>= 1
        return ret


G = []


def ope_1(x: int):
    pass


def ope_2(x: int, k: int):
    pass


def ope_3(x: int, k: int):
    pass


Q = int(input())

commands = []

for i in range(Q):
    commands.append(list(map(int, input().split())))

for command in commands:
    if command[0] == 1:
        ope_1(command[1])
    elif command[0] == 2:
        x, k = command[1:]
        ope_2(x, k)
    elif command[0] == 3:
        x, k = command[1:]
        ope_3(x, k)
