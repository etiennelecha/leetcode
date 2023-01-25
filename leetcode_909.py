from collections import deque
from typing import List


class Solution:
    """
    no input reindixing, beats ~30% compute, beats ~60% memory
    Complexity: Compute O(n^2), Memory O(n^2)
    """

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def bfs(even):
            q = deque([(n - 1, 0)])
            visited = set()
            steps = 0
            target = 0, 0 if even == 1 else n - 1
            while q:
                l = len(q)
                for _ in range(l):
                    x, y = q.popleft()
                    if (x, y) == target:
                        return steps
                    if (x, y) in visited:
                        continue
                    for c in candidates(x, y, even):
                        xx, yy = c
                        if board[xx][yy] != -1:
                            c = converter(board[xx][yy], even)
                        q.append(c)
                    visited.add((x, y))
                steps += 1
            return -1

        def get_even(k):
            return 1 if k % 2 == 0 else -1

        def candidates(x, y, even):
            ans = []
            target = 0, 0 if even == 1 else n - 1
            for _ in range(6):
                if 0 <= y - even * get_even(x) <= n - 1:
                    ans.append((x, y - even * get_even(x)))
                    y -= even * get_even(x)
                elif (x, y) != target:
                    x -= 1
                    ans.append((x, y))
                else:
                    break
            return ans

        def converter(pos, even):
            x = (n - 1) - (pos - 1) // n
            y = (pos - 1) % n if get_even(x) * even == -1 else n - 1 - (pos - 1) % n
            return x, y

        even = get_even(n)
        return bfs(even)
