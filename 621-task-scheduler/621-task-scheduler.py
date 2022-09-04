from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        c = Counter(tasks)
        if n == 0:
            return c.total()
        while c.total()>0:
            mc = c.most_common()
            if c.total()<=n and mc[0][1] == 1:
                return ans+c.total()
            if len(mc)<=n:
                ans += n+1
                for i in c:
                    if c[i]>0:
                        c[i]-=1
            else:
                for j in mc[:n+1]:
                    i = j[0]
                    if c[i]>0:
                        c[i]-=1
                        ans+=1
            c = Counter({x:y for x,y in c.items() if y!=0})
        return ans
                
                