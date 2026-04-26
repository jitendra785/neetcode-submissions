class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num1_idx, num1 in enumerate(numbers):
            for num2_idx, num2 in enumerate(numbers):
                if (num1_idx < num2_idx) and (num1 + num2 == target):
                    return [num1_idx+1, num2_idx+1]
        return []
        