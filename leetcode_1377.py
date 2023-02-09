from collections import deque, defaultdict
from typing import List


class Solution:
    """
    LC hard.
    find the probability of going to a certain node in a tree after a certain number of steps,
    plus some special conditions when you are at a leaf (you can 'wait' there as much as you want)
    Not so hard once you realize there is only one path to a node in a tree if it is directed,
    which it effectively is here.
    TC O(n) beats ~76% MC O(n) beats ~88%
    """

    def frogPosition(
        self, n: int, edges: List[List[int]], t: int, target: int
    ) -> float:
        if target == 1:
            if not t or not edges:
                return 1
            return 0
        neighbors = defaultdict(list)
        for u, v in edges:
            neighbors[u] += [v]
            neighbors[v] += [u]
        q = deque([(u, 1, len(neighbors[1]) ** -1) for u in neighbors[1]])
        steps = 1
        while q:
            l = len(q)
            for _ in range(l):
                u, prev, prob = q.popleft()
                if u == target:
                    if steps == t or steps < t and len(neighbors[u]) == 1:
                        return prob
                    return 0
                for v in neighbors[u]:
                    if v == prev:
                        continue
                    q.append((v, u, prob * (len(neighbors[u]) - 1) ** -1))
            if steps > t:
                return 0
            steps += 1
        return 0
