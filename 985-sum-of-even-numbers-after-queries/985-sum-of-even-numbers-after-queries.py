class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        evSum = 0
        for num in nums:
            if num%2==0:
                evSum += num
        for val,index in queries:
            if nums[index]%2 == 0:
                evSum -= nums[index]
            nums[index] = nums[index] + val
            if nums[index]%2 == 0:
                evSum += nums[index]
            answer.append(evSum)
        return answer