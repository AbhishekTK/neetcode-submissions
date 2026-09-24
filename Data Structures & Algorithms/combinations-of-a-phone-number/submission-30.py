class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        s = [""]
        for i in digits:
            ss = []
            for j in digitToChar[i]:
                for e in s:
                    e = e+j
                    ss.append(e)
            s = ss

        return s