class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        table = {
            1000: 'M',
            900: 'CM', 
            500: 'D', 
            400: 'CD', 
            100: 'C', 
            90: 'XC', 
            50: 'L', 
            40: 'XL', 
            10: 'X', 
            9: 'IX', 
            5: 'V',
            4: 'IV', 
            1: 'I'
        }
        arr = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        for n in arr:
            while num >= n:
                num -= n
                res += table[n]
        return res