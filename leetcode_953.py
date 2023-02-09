from typing import List


class Solution:
    """
    LC EZ. TC: O(n), Space complexity O(1). Beats ~95% compute, ~75% memory
    """

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        order_dic = {k: v for v, k in enumerate(order)}
        for i in range(n - 1):
            for c1, c2 in zip(words[i], words[i + 1]):
                if order_dic[c1] < order_dic[c2]:
                    break
                if order_dic[c1] > order_dic[c2]:
                    return False
            else:
                if len(words[i]) > len(words[i + 1]):
                    return False
        return True
