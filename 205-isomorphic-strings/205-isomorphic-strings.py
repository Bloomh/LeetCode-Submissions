class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        check = ""
        for char_s,char_t in zip(s,t):
            if char_s not in s_to_t and char_t not in t_to_s:
                s_to_t[char_s] = char_t
                t_to_s[char_t] = char_s
            elif char_s in s_to_t and char_t in t_to_s and s_to_t[char_s] == char_t and t_to_s[char_t] == char_s:
                continue
            else:
                return False
        return True