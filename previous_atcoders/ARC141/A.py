

def get_divisor(num):
    ans = [i for i in range(1, num) if num % i == 0]
    return ans


T = int(input())

nums = []
for i in range(T):
    num = input()
    nums.append(num)

ans_list = []

for num in nums:
    size = len(num)
    divisor = get_divisor(size)[::-1]
    best = -1
    for div in divisor:
        i = 0
        parts = []
        while size - i >= div:
            parts.append(num[i:i+div])
            i = i + div
        # print(parts)
        head = int(parts[0])
        length = size // div
        for h in reversed(range(head+1)):
            ans = int("".join([str(h)] * length))
            if ans <= int(num) and h != 0:
                if best < ans:
                    best = ans
                break
            else:
                if len(str(h)) < len(str(head)) or h == 0:
                    ans = int("".join(["9"] * (size-1)))
                    if best < ans:
                        best = ans
                    break
    ans_list.append(str(best))

# print("ans_list: ", ans_list)

for ans in ans_list:
    print(ans)
