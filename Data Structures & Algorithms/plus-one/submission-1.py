class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if carry + digits[i] < 10:
                digits[i] = carry+digits[i]
                carry = 0
            else:
                digits[i] = (carry+digits[i])%10
                carry = 1
        if carry != 0:
            digits.insert(0,carry)

        return digits


            
        