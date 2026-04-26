class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = b""
        for str_ in strs:
            n = len(str_)
            encoded_strs += str_.encode() + b"~"
        return encoded_strs.decode('utf-8') 

    def decode(self, s: str) -> List[str]:
        strs = []
        encoded_strs = list(s.split('~'))
        for encoded_str in encoded_strs[:-1]:
            strs.append(
                encoded_str
            )
        return strs

