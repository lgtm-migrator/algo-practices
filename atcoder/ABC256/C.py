from itertools import product

h1, h2, h3, w1, w2, w3 = map(int, input().split())

h1_candidates = list(filter(lambda x: sum(x) == h1,
                     product(range(1, h1-1), repeat=3)))
h2_candidates = list(filter(lambda x: sum(x) == h2,
                     product(range(1, h2-1), repeat=3)))
h3_candidates = list(filter(lambda x: sum(x) == h3,
                     product(range(1, h3-1), repeat=3)))

h3_w1_set = set(list(map(lambda x: x[0], h3_candidates)))
h3_w2_set = set(list(map(lambda x: x[1], h3_candidates)))
h3_w3_set = set(list(map(lambda x: x[2], h3_candidates)))


ans = 0

for h1_candidate in h1_candidates:
    stop = False
    # print("h1_candidate", h1_candidate)
    remain_w1 = w1 - h1_candidate[0]
    remain_w2 = w2 - h1_candidate[1]
    remain_w3 = w3 - h1_candidate[2]

    for h2_candidate in h2_candidates:
        if stop:
            break
        # print("h2_candidate[0]", h2_candidate[0])
        # print("h2_candidate[1]", h2_candidate[1])
        # print("h2_candidate[2]", h2_candidate[2])
        remain_w1_2 = remain_w1 - h2_candidate[0]
        remain_w2_2 = remain_w2 - h2_candidate[1]
        remain_w3_2 = remain_w3 - h2_candidate[2]

        if remain_w1_2 <= 0 or remain_w2_2 <= 0 or remain_w3_2 <= 0:
            continue

        # print("remain_w1", remain_w1_2)
        # print("remain_w2", remain_w2_2)
        # print("remain_w3", remain_w3_2)

        if remain_w1_2 + remain_w2_2 + remain_w3_2 != h3:
            continue

        if remain_w1_2 in h3_w1_set and remain_w2_2 in h3_w2_set and remain_w3_2 in h3_w3_set:
            ans += 1
            # print("Added", remain_w1_2, remain_w2_2, remain_w3_2)

print(ans)
