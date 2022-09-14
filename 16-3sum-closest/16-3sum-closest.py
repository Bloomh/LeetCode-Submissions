class Solution:
    def threeSumClosest(self, num, target):
        num.sort() #sort
        result = num[0] + num[1] + num[2] #start w this result
        n = len(num) #length
        for i in range(n - 2): #iterate through rest
            if i > 0 and num[i] == num[i-1]: #if multiple in a row then we will explore this possibility another time
                continue
            j, k = i+1, n - 1 #1 after the element up to the end
            while j < k: #iterate up to when the sliding window collapses
                sm = num[i] + num[j] + num[k] #temp new sum
                if sm == target:
                    return sm #return answer if we can get it perfectly
                
                if abs(sm - target) < abs(result - target): #update answer if we have better
                    result = sm 
                
                if sm < target: #if too small then move middle up
                    j += 1
                elif sm > target: #if too big then move right down
                    k -= 1
            
        return result