class TrieNode:
    def __init__(self):
        self.ch = {}
        self.w = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.ch:
                cur.ch[c] = TrieNode()
            cur = cur.ch[c]
        cur.w = True

    def search(self, word: str) -> bool:

        def dfs(j,root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.ch.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in cur.ch:
                        return False
                    cur = cur.ch[c]
            return cur.w
        return dfs(0,self.root)
