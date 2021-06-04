from typing import List


class Solution:
    def rotate(self, nums:List[int], k: int)-> None:
        # nums =
        nums1 = list()
        for i in range(k):
            nums1.append(nums.pop())
        nums1.reverse()
       
        nums1.extend(nums)
        return nums1



Solution.rotate(Solution,[1,2,3,4,5,6,7],3)