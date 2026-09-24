class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        s = [""]
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
        for d in digits:
            sc = []
            for ss in s:
                cs = di[d]
                for c in cs:
                    sc.append(ss+c)
            s = sc
        return s