from heapq import heappush, heappop, heapify


class SegmentTree:
    def __init__(self):
        # Heap
        self.h = []
        # HeapDict
        self.d = dict()

    def insert(self, x: int):
        heappush(self.h, x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    def erase(self, x: int, cnt: int = 1):
        if x not in self.d or self.d[x] == 0:
            return
        else:
            self.d[x] -= cnt

        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heappop(self.h)
            else:
                break

    def get_min(self):
        return self.h[0]

    def get_cnt(self, x: int):
        return self.d[x] if self.d[x] is not None else 0

    def is_exist(self, x: int) -> bool:
        if self.d[x] is None or self.d[x] == 0:
            return False
        return True
