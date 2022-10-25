from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for idx in range(0, len(nums), 2):
            answer += min(nums[idx], nums[idx + 1])
        return answer