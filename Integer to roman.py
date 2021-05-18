class Solution:
    def intToRoman(self, num: int) -> str:
        list1 = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        list2= ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        i=12
        s=''
        while num:
            n = num//list1[i]
            num %= list1[i]
            s+=list2[i]*n
            i-=1
        return s
