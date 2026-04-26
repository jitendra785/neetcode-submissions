class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        res_keys = []
        for num in nums:
            if num not in res_keys:
                res_keys.append(num)
                res[num] = 1
            else:
                res[num] += 1
        sorted_dict = {ke: v for ke, v in sorted(res.items(), key=lambda item: item[1], reverse=True)}
        sorted_dict_keys = list(sorted_dict.keys())
        return [int(ke) for ke in sorted_dict_keys[:k]]  
        

        