class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.i = 0

        def parse():
            result = set()

            while self.i < len(expression) and expression[self.i] != "}":
                term = parse_term()
                result |= term

                if self.i < len(expression) and expression[self.i] == ",":
                    self.i += 1

            return result

        def parse_term():
            result = {""}

            while self.i < len(expression):
                if expression[self.i] in "},":
                    break

                if expression[self.i] == "{":
                    self.i += 1
                    current = parse()
                    self.i += 1
                else:
                    current = {expression[self.i]}
                    self.i += 1

                new_result = set()

                for a in result:
                    for b in current:
                        new_result.add(a + b)

                result = new_result

            return result

        return sorted(parse())