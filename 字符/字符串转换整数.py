class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)
        result = 0
        sign = 1  # 默认为正数

        # 跳过前导空格
        while i < n and s[i] == ' ':
            i += 1

        # 检查正负号
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 读取数字字符
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # 检查溢出
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
还是//10和%10那点事
