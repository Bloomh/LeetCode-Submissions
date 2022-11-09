class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter(nums)
        try:
            return sorted(list(set(num for num in nums if num%2==0)), key = lambda x:(-c[x],x))[0]
        except:
            return -1