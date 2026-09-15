class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"*", "-", "+", "/"}
        for i in tokens:
            if i in operators:
                two = int(stack.pop())
                one = int(stack.pop())

                match i:
                    case "*":
                        stack.append(one * two)
                    case "-":
                        stack.append(one - two)
                    case "+":
                        stack.append(one + two)
                    case "/":
                        stack.append(int(one / two))

                    

            else:
                stack.append(int(i))

        return stack[-1]
                