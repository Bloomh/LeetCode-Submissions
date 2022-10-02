class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magCounter = Counter(magazine)
        for letter in set(ransomNote):
            if ransomCounter[letter]>magCounter[letter]:
                return False
        return True