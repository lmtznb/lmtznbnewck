class Solution:
    def countSegments(self, s):
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count

solution = Solution()

# 使用 countSegments 方法计算字符串中单词的数量
input_string = "Hello, world, this is a test."
word_count = solution.countSegments(input_string)

print(word_count)