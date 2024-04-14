"""
3 1 1
1 1 1
1 1 1
1 1 1
2 3 7
"""
from collections import deque

N, M, K = map(int, input().split())
farm = list()
for r in range(N):
    row = list(map(int, input().split()))
    farm.append([{"f_now": 5, "f_add": f_add} for f_add in row])

trees = deque()
for i in range(M):
    r, c, z = map(int, input().split())
    trees.append({"r": r - 1, "c": c - 1, "age": z})

#
for i in range(K):
    dead_trees = []
    live_trees = deque()

    for tree in trees:
        r = tree["r"]
        c = tree["c"]
        f_now = farm[r][c]["f_now"]

        if (f_now - tree["age"]) < 0:
            dead_trees.append(tree)
        else:
            farm[r][c]["f_now"] = f_now - tree["age"]
            tree["age"] = tree["age"] + 1
            live_trees.append(tree)

    for t in dead_trees:
        farm[t["r"]][t["c"]]["f_now"] += t["age"] // 2
    trees = live_trees

    new_trees = []
    for idx in range(len(trees)):
        r = trees[idx]["r"]
        c = trees[idx]["c"]
        f_now = farm[r][c]["f_now"]

        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]
        if trees[idx]["age"] % 5 == 0:
            for dx, dy in zip(dr, dc):
                if r + dx < 0 or r + dx >= N: continue
                if c + dy < 0 or c + dy >= N: continue
                new_trees.append({"r": r + dx, "c": c + dy, "age": 1})
    trees.extendleft(new_trees)

    for r in range(N):
        for c in range(N):
            farm[r][c]["f_now"] = farm[r][c]["f_now"] + farm[r][c]["f_add"]

print(len(trees))
