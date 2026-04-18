class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        print(tokens)
        for token in tokens:
            if token not in ['+','-','*','/']:
                operands.append(int(token))
            else: 
                b = operands.pop()
                a = operands.pop()
                if token == "+":
                    operands.append(a+b)
                if token == "-":
                     operands.append(a-b)
                if token=="*":
                    operands.append(a*b)
                if token=="/":
                    operands.append(int(float(a)/b))
        print(operands)
        return operands[0]    
            

