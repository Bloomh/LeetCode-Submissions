class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        numBulls = 0
        numCows = 0
        cSecret = Counter(secret)
        for i,digit in enumerate(guess):
            if digit == secret[i]:
                numBulls += 1
                if cSecret[digit] == 0:
                    numCows -= 1
                else:
                    cSecret[digit] -= 1

            elif digit in cSecret and cSecret[digit] >= 1:
                numCows += 1
                cSecret[digit] -= 1
        return str(numBulls) + "A" + str(numCows) + "B"