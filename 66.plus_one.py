class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        overflow = 1
        for index in range(len(digits)-1,-1,-1):
            digit = digits[index]
            digits[index]= (digit+1)%10
            overflow = (digit+1)//10
            if not overflow:
                break
        if overflow:
            digits.insert(0,1)
        return digits

        
