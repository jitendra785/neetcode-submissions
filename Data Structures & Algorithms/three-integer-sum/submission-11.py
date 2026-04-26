class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        for idx_i, i in enumerate(nums):
            for idx_j, j in enumerate(nums):
                if (idx_i != idx_j):
                    for idx_k, k in enumerate(nums):
                        if (idx_i != idx_k) and (idx_j != idx_k) and (i+j+k ==0):
                            s1=tuple(sorted((i,j,k)))
                            triplets.add(s1)
        return [list(s) for s in triplets]



        