class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        return list(set(list(s1.intersection(s2))+list(s2.intersection(s3))+list(s1.intersection(s3))))