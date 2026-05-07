class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            completent = target - value
            if completent in seen:
                return [seen[completent], index]
            seen[value] = index