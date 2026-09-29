class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for s in strs:
            encoded_strs += str(len(s)) + "%" + s
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "%":
                j += 1
            length = int(s[i:j])
            start = j + 1
            decoded_strs.append(s[start:start + length])
            i = start + length
        return decoded_strs