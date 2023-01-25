from typing import List


class Solution:
    """
    LC hard. Longest cycle in a directed graph with at most one outgoing edge. 
    Strongly inspired by Tarjan's algorithm.
    TC O(edges), MC O(edges). Beats 93% compute, 95% memory
    """

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        i = 0
        ans = -1
        visited = [-1] * n
        counter = 0
        for i in range(n):
            if visited[i] >= 0 or edges[i] < 0:
                continue
            ptr = i
            start = counter
            while edges[ptr] >= 0 and visited[ptr] == -1:
                visited[ptr] = counter
                counter += 1
                ptr = edges[ptr]
            if edges[ptr] >= 0 and visited[ptr] >= start:
                ans = max(ans, counter - visited[ptr])
        return ans
