all = set(range(0, 10))

if __name__ == "__main__":
    nums = set(map(int, map(str, input()))) ^ all
    print(nums.pop())
