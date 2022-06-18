N = int(input())

nums = list(map(int, input().split()))

score = 0


class Object:
    def __init__(self, position, is_goal=False):
        self.position = position
        self.is_goal = is_goal

    def move(self, x: int):
        if self.is_goal:
            return
        global score
        self.position += x
        if self.position >= 4:
            score += 1
            self.is_goal = True


objects = []

for num in nums:
    objects.append(Object(0))
    for object in objects:
        object.move(num)

print(score)
