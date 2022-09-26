class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        def find(x):
            if x not in parent:
                return x
            else:
                return find(parent[x])
        for i in equations:
            if i[1]=="=": #check all equalities
                a = i[0]
                b = i[-1]
                x = find(a)
                y = find(b)
                if x!=y: #if they dont have the same parent
                    parent[y] = x #set the second to be the parent of the first
        for i in equations:
            if i[1]=="!" and find(i[0])==find(i[-1]): #if they have the same parent and are not supposed to equal each other, then we have failed
                return False
        return True
                        
                    
                    