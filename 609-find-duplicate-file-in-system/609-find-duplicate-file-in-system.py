class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dct = {}
        ansKeys = []
        for i in paths:
            lst = i.split(" ")
            root = lst[0]
            for j in range(1,len(lst)):
                contStart = lst[j].index("(")
                path = root+"/"+lst[j][:contStart]
                content = lst[j][contStart+1:-1]
                if content in dct:
                    if content not in ansKeys:
                        ansKeys.append(content)
                    dct[content].append(path)
                else:
                    dct[content] = [path]
        return [dct[i] for i in ansKeys]