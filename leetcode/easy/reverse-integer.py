# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if int(str(abs(x))[::-1]) > 2 ** 31 - 1:
            return 0
        if x > 0:
            return int(str(x)[::-1])
        else:
            return -1 * int(str(abs(x))[::-1])
