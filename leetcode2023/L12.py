# leetcode 12. Integer to Roman
# https://leetcode-cn.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        if num < 1: return ""
        if num > 3999: return "M*"
        one = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
        two = {0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
        three = {0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
        four = {0: "", 1: "M", 2: "MM", 3: "MMM"}
        return four[num // 1000] + three[num % 1000 // 100] + two[num % 100 // 10] + one[num % 10]