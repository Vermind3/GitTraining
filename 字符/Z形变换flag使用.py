class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)

关键在于flag的使用，和把z字形看作三个数组，在python中未必是二维数组，而是以维数组
这里我突然意识到学习其他人算法的好处，在解决一个问题的时候，如果你不了解大部分人是怎么做的，
即使你是一个天才，你依然需要去想每一个方法，甚至是去发明每一个方法
而如果你早就学会了大部分方法，你可以很快的套用在该问题上，发现都行不通之后，哪怕需要再发明一个
新的方法，也无需那么费劲
