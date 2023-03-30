class Solution:
    def myAtoi(self, str: str) -> int:
        type = "1"
        a = ""
        k = 0
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if str == "": return 0
        for n in range(len(str)):
            if a != "" and str[n] not in num: break
            if str[n] == " " and n == len(str) - 1: return 0
            if str[n] == " " and (type == "+1" or type == "-1"): return 0
            if str[n] == " ": continue
            if str[n] not in num and str[n] != "-" and str[n] != "+" and k == 0: return 0
            if (str[n] == "-" or str[n] == "+") and k != 0:
                break
            elif str[n] == "-" and k == 0 and (type != "+1" and type != "-1"):
                type = "-1"
            elif str[n] == "+" and k == 0 and (type != "+1" and type != "-1"):
                type = "+1"
            elif str[n] == "+" and k == 0 and (type == "+1" or type == "-1"):
                return 0
            elif str[n] == "-" and k == 0 and (type == "+1" or type == "-1"):
                return 0
            if str[n] in num and (k == 1 or k == 0):
                k = 1
                a = a + str[n]
        if (type == "-1" or type == "+1") and a == "": return 0
        if int(type) * int(a) < -2 ** 31: return -1 * 2 ** 31
        if int(type) * int(a) > 2 ** 31 - 1: return 2 ** 31 - 1
        return int(type) * int(a)