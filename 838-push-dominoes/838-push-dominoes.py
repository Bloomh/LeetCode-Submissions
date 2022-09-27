class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        lft = [float('inf')]
        rght = [float('inf')]
        for i in range(1,n):
            if dominoes[i]!='L':
                if dominoes[i-1] == 'R':
                    rght.append(1)
                else:
                    rght.append(min(rght[-1]+1,float('inf')))
            else:
                rght.append(float('inf'))
            
            if dominoes[-i-1]!='R':
                if dominoes[-i]=='L':
                    lft.append(1)
                else:
                    lft.append(min(lft[-1]+1,float('inf')))
            else:
                lft.append(float('inf'))
            # rght.append((dominoes[i-1]=='R' or rght[i-1]) and dominoes[i]!='L')
            # lft.append((dominoes[-i]=='L' or lft[i-1]) and dominoes[-i-1]!='R')
        lft = lft[::-1]
        ans = ""
        for i in range(n):
            if dominoes[i] == ".":
                if rght[i]<lft[i]:
                    ans+='R'
                elif lft[i]<rght[i]:
                    ans+='L'
                else:
                    ans+='.'
            else:
                ans+=dominoes[i]
        return ans