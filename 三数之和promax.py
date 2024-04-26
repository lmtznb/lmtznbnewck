from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    #排序
    result = []
    n = len(nums)

    # 遍历所有可能的 a
    for i in range(n - 2):
        # 跳过重复元素
        if i > 0 and nums[i] == nums[i - 1]:
            continue

            # 初始化 b 和 c 的指针
        left = i + 1
        right = n - 1

        # 使用 target 变量存储 -nums[i]，方便后续计算
        target = -nums[i]

        # 遍历所有可能的 b 和 c 组合
        while left < right:
            current_sum = nums[left] + nums[right]

            # 如果当前和等于 target
            if current_sum == target:
                # 确保 b 的位置与 a 不同
                if left != i:
                    result.append([nums[i], nums[left], nums[right]])

                    # 跳过重复元素
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                    # 移动 b 和 c 的指针以寻找下一组解
                left += 1
                right -= 1

                # 如果当前和小于 target，移动 b 的指针
            elif current_sum < target:
                left += 1
                # 如果当前和大于 target，移动 c 的指针
            else:
                right -= 1

    return result


# 示例
nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(result)