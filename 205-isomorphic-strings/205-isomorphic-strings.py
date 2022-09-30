class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {} #letters in s mapped to letters in t
        t_to_s = {} #t mapped to s
        for char_s,char_t in zip(s,t): #go through characters in s and t
            if char_s not in s_to_t and char_t not in t_to_s: #if neither element is mapped
                s_to_t[char_s] = char_t 
                t_to_s[char_t] = char_s 
            else:
                try: 
                    if not (s_to_t[char_s] == char_t and t_to_s[char_t] == char_s):
                        return False 
                except: 
                    return False #so we return false
        return True