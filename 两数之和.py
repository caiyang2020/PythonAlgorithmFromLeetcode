class Solution:
    def twoSum(self,nums:[int],target:int):
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]

if __name__ == "__main__":
    test1 = Solution()
    sum1=test1.twoSum([1,2,3,4,5,6,7,8,9],10)
    # test1 = Solution().twoSum(123123,123123)
    print(sum1)

