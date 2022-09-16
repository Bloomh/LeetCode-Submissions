class Trie:

    def __init__(self):
        self.dc = {}

    def insert(self, word: str) -> None:
        self.dc[word] = 2
        for i in range(len(word)-1,0,-1):
            if word[:i] not in self.dc:
                self.dc[word[:i]] = 1
            else:
                break

    def search(self, word: str) -> bool:
        return (word in self.dc) and self.dc[word] == 2

    def startsWith(self, prefix: str) -> bool:
        return (prefix in self.dc)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)