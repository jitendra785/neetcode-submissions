class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        if 3 <= len(nums) <= 1000:
            for idx_i, i in enumerate(nums):
                for idx_j, j in enumerate(nums):
                    if (idx_i != idx_j):
                        for idx_k, k in enumerate(nums):
                            if (idx_i != idx_k) and (idx_j != idx_k) and (i+j+k ==0):
                                l1=[i,j,k]
                                l1.sort()
                                if l1 not in triplets:
                                    triplets.append(l1)
        return triplets



        