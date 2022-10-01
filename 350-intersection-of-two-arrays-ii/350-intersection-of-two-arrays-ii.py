class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1)>len(nums2): 
            nums2,nums1 = nums1,nums2 #make sure nums1 is the smaller one
        c1 = Counter(nums1) #keep track of the counts of everything in nums1
        
        ans = [] #answer array
        for num in nums2: #go through every number
            if num in c1 and c1[num] > 0: #if it exists in the counter
                ans.append(num) #add it to the answer list
                c1[num] -= 1
        return ans
        
        