nums = [2, 7, 11, 15]
target = 9
seen = set()  # 用于记录已经输出过的索引对

for i in range(len(nums)):
    for j in range(i, len(nums)):  # 从i开始，避免重复计算
        if nums[i] + nums[j] == target and (i, j) not in seen:
            seen.add((i, j))  # 添加索引对到集合中
            print(nums[i], nums[j])
