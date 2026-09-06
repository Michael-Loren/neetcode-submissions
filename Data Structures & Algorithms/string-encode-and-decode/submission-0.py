class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s += (f"{len(string)}#{string}")
        return s


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        decoded_str = ""
        readingstring = False
        num = ""
        for char in s:
            if not readingstring:
                if char != "#":
                    num += char
                else:
                    readingstring = True
                    num = int(num)
                    if num == 0:
                        num = ""
                        decoded_strs.append(num)
                        readingstring = False

            else:
                decoded_str += char
                num -= 1
                if num == 0:
                    num = ""
                    readingstring = False
                    decoded_strs.append(decoded_str)
                    decoded_str = ""
        return decoded_strs

            


    
