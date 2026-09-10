class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        print(stack)

        for i, n in enumerate(temperatures):
            print("stack", stack)
            while stack and n > stack[-1][0]:
                m, j = stack.pop()
                print(m, j)
                res[j] = i - j
            stack.append((n, i))

        return res