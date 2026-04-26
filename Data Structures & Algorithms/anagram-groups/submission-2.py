class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        temp = []
        for idx, str_1 in enumerate(strs):
            if idx not in temp:
                sublist = [str_1]
                temp.append(idx)
                for idx_2, str_2 in enumerate(strs):
                    if (sorted(str_1) == sorted(str_2)) and (idx_2 not in temp):
                        sublist.append(str_2)
                        temp.append(idx_2)
                res.append(sublist)
        return res

        