class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                n1 = stack.pop()
                n1 += stack.pop()
                stack.append(n1)
            elif t == "-":
                n1 = stack.pop()
                n1 -= stack.pop()
                stack.append(-n1)
            elif t == "*":
                n1 = stack.pop()
                n1 *= stack.pop()
                stack.append(n1)
            elif t == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                n2 = n2 / n1 if n1 != 0 else 0
                stack.append(int(n2))
            else:
                stack.append(int(t))
            print(stack)
        
        return stack[-1]
