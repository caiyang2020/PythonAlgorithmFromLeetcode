"""给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。"""
class Solution:
    def removeDuplicates(self,nums):
        
        for i in range(len(nums)):
            num = nums[i]
            if i+1 < len(nums):
                if num == nums[i+1]:
                    nums.pop(i+1)
                    return Solution.removeDuplicates(Solution,nums)

        return len(nums)


  
        

if __name__=="__main__":
    list1 = [0,0,1,1,1,2,2,3,3,4]
    test = Solution()
    print(test.removeDuplicates(list1))