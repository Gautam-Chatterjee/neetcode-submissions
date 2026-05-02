class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        output = deque([])
        for i in range(len(digits)-1,-1,-1):
            if carry + digits[i] < 10:
                output.appendleft(carry+digits[i])
                carry = 0
            else:
                output.appendleft((carry+digits[i])%10)
                carry = 1
        if carry != 0:
            output.appendleft(carry)
        return list(output)


            
        