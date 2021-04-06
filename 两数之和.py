"""
    nums为一个由int类型组成的数组
    target为一个int 类型的数据
    输入target 在nums中寻找有没有两个数能组合成target
    返回两个数的位置
"""

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

