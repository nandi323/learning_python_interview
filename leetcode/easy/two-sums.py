# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_list = len(nums)
        for idx, i in enumerate(nums):
            item_searched = target - i
            if item_searched in nums:
                idj = nums.index(item_searched)
                if idj != idx:
                    return (idx, idj)
