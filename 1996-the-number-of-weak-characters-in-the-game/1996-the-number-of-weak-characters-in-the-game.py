class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1]))
        ans = 0
        mx = 0
        
        for i in properties:
            if i[1]<mx:
                ans+=1
            else:
                mx = i[1]
        return ans