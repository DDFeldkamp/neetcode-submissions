class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ''
        for s in strs:
            final += str(len(s)) + '#' + s
        return final

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            delim_pos = s.find('#', i)
            length = int(s[i:delim_pos])
            res.append(s[delim_pos + 1 : delim_pos + 1 + length])
            i = delim_pos + 1 + length
        return res