class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = collections.deque([(start,0)])
        
        while q:
            gene, mutations = q.popleft()
            if gene == end:
                return mutations
            i = 0
            while i < len(bank):
                bankgene = bank[i]
                if sum([x==y for (x,y) in zip(gene,bankgene)]) == 7:
                    q.append((bankgene, mutations+1))
                    bank.pop(i)
                else:
                    i += 1
            
        return -1