class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_consecutive_seqs = [1]
        nums = list(set(nums))
        nums.sort()
        from_idx = 0
        max_consecutive_seq = 1
        for i in range(len(nums)):
            if i != 0:
                if abs(nums[i] - nums[i-1]) == 1:
                    max_consecutive_seq += 1
                    max_consecutive_seqs.append(max_consecutive_seq)
                else:
                    from_idx += 1
                    max_consecutive_seqs.append(max_consecutive_seq)
                    max_consecutive_seq = 1
        return max(max_consecutive_seqs)
                    


