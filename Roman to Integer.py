class Solution:
    def romanToInt(self, s: str) -> int:
        sums = 0
        if "IX" in s:sums += s.count("IX")*9
        s=s.replace("IX","")
        if "IV" in s:sums += s.count("IV")*4
        s=s.replace("IV","")
        if "XL" in s:sums += s.count("XL")*40
        s=s.replace("XL","")
        if "XC" in s:sums += s.count("XC")*90
        s=s.replace("XC","")
        if "CD" in s:sums += s.count("CD")*400
        s=s.replace("CD","")
        if "CM" in s:sums += s.count("CM")*900
        s=s.replace("CM","")
        sums += s.count("I")*1
        sums += s.count("V")*5
        sums += s.count("X")*10
        sums += s.count("L")*50
        sums += s.count("C")*100
        sums += s.count("D")*500
        sums += s.count("M")*1000
        return sums
