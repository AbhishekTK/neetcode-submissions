class Solution:
    def decodeString(self, s: str) -> str:

        st = []
        # r = ""

        for i in range(len(s)):
            if s[i] !="]":
                st.append(s[i])
            else:
                see = ""
                while st[-1] != "[":
                    see = st.pop()+see
                st.pop()
                k = ""
                while s and s[-1].isdigit():
                    k = st.pop()+k
                st.append(int(k)*see)
        return "".join(st)