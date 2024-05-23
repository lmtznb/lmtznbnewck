from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]
        return max(a, b)


# 创建Solution类的实例
sol = Solution()

# 测试数组
nums = [-1, -99, -3, -4, 2, -555, 3, 4, 4, 6, 8, 77]

# 调用方法并打印结果
print(sol.maximumProduct(nums))  # 应该输出最大的乘积