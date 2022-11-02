class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = collections.deque([(start,0)])
        bank = set(bank)
        
        while q:
            gene, mutations = q.popleft()
            if gene == end:
                return mutations
            for bankgene in set(bank):
                if sum([x==y for (x,y) in zip(gene,bankgene)]) == 7:
                    q.append((bankgene, mutations+1))
                    bank.remove(bankgene)
            
        return -1