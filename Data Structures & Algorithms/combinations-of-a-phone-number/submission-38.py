class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        s = [

        ]
        di = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def b(i,cs):
            if len(cs)==len(digits):
                s.append(cs)
                return
            for c in di[digits[i]]:
                b(i+1,cs+c)
        if digits:
            b(0,"")
        return s