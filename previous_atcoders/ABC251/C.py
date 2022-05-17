class Submission(object):
    def __init__(self, i: int, text: str, score: int):
        self.i = i
        self.text = text
        self.score = score

    def __eq__(self, o):
        if not isinstance(o, Submission):
            return False
        return o.text == self.text

    def __hash__(self):
        return hash(self.text)

    def __str__(self):
        return f"i: {self.i}, text: {self.text}, score: {self.score}"


class Manager:
    def __init__(self):
        self.submissions = set()

    def add(self, new_submission: Submission):
        if new_submission in self.submissions:
            return
        self.submissions.add(new_submission)

    def top(self) -> Submission:
        best = None
        for submission in list(self.submissions):
            if best is None or best.score < submission.score:
                best = submission
        return best


N = int(input())
m = Manager()
for i in range(1, N + 1):
    inputs = input().split(" ")
    S = inputs[0]
    T = int(inputs[1])
    sub = Submission(i, S, T)
    m.add(sub)

ans = m.top().i
print(ans)
