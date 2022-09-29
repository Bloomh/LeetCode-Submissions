class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {} #letters in s mapped to letters in t
        t_to_s = {} #t mapped to s
        # for char_s,char_t in zip(s,t): #go through characters in s and t
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]  
            if char_s not in s_to_t and char_t not in t_to_s: #if neither element is mapped
                s_to_t[char_s] = char_t #map s to t
                t_to_s[char_t] = char_s #map t to s
            elif char_s in s_to_t and char_t in t_to_s and s_to_t[char_s] == char_t and t_to_s[char_t] == char_s: #otherwise if the characters in s and t are properly mapped to each other
                continue #then we can continue
            else: #at least one of the elements is mapped to something different!
                return False #so we return false
        return True