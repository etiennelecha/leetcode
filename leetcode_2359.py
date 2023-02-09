from typing import List


class Solution:
    """
    minimum distances in a graph with only one outgoing edge per node
    TC = O(n), MC = O(n) beats 83% time, beats 77% memory
    """

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def distances(start):
            ans = [10**5] * n
            ptr = start
            steps = 0
            while ptr != -1 and ans[ptr] == 10**5:
                ans[ptr] = steps
                steps += 1
                ptr = edges[ptr]
            return ans

        distances1 = distances(node1)
        distances2 = distances(node2)
        ans = min(range(n), key=lambda x: max(distances1[x], distances2[x]))
        return ans if max(distances1[ans], distances2[ans]) != 10**5 else -1
