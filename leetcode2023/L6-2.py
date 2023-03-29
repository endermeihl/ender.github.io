class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)==0 or numRows == 1:return s
        r = ""
        l = int(len(s) / (2 * numRows - 2))
        re = 2 * (numRows - 1)
        for n in range(0, numRows):
            for i in range(0, l + 1):
                if (n + (numRows - 1) * i * 2) % re == 0 and n + (numRows - 1) * i * 2 < len(s):
                    r = r + s[n + (numRows - 1) * i * 2]
                    continue
                elif (n + (numRows - 1) * i * 2) % re == numRows - 1 and n + (numRows - 1) * i * 2 < len(s):
                    r = r + s[n + (numRows - 1) * i * 2]
                    continue
                if (n + (numRows - 1) * i * 2) % re == n and n + (numRows - 1) * i * 2 < len(s):
                    r = r + s[n + (numRows - 1) * i * 2]
                if (n + (numRows - 1) * i * 2) % re == n and re * (2*i + 1) - (n + (numRows - 1) * i * 2) < len(s):
                    r = r + s[re * (2*i + 1) - (n + (numRows - 1) * i * 2)]
        return r