class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        uniqueChars = set()
        for letter in sentence:
            uniqueChars.add(letter)
            if len(uniqueChars) == 26:
                return True
        return False