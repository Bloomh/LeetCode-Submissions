class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        @lru_cache
        def helper(f, N, K):
            if N == 1:
                return [f]
            ret = []
            if f>=K:
                h = helper(f-K,N-1,K)
                if h:
                    ret.extend([i+10**(N-1)*f for i in h])
            if f+K<=9:
                h = helper(f+K,N-1,K)
                if h:
                    ret.extend([i+10**(N-1)*f for i in h])
            return ret
        for i in range(1,10):
            h = helper(i,n,k)
            if h:
                ans.extend(h)
        return set(ans)