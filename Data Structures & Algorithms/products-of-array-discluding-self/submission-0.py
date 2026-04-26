class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            product = None
            for j in range(len(nums)):
                if i!=j:
                    if product is not None:
                        product *= nums[j]
                    else:
                        product = nums[j]
            result.append(product)
        return result