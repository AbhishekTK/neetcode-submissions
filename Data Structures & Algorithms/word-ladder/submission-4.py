class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if (endWord not in wordList ) or (beginWord ==endWord):
            return 0
        mp = {}
        n,m = len(wordList),len(wordList[0])
        for i,w in enumerate(wordList):
            mp[w] = i
        adj  = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                c = 0
                for k in range(m):
                    if wordList[i][k]!=wordList[j][k]:
                        c+=1
                if c==1:
                    adj[i].append(j)
                    adj[j].append(i)
        
        q,r = deque(),1
        v = set()
        for i in range(m):
            for c in range(97,123):
                if chr(c)==beginWord[i]:
                    continue
                word = beginWord[:i]+chr(c)+beginWord[i+1:]
                if word in mp and mp[word] not in v:
                    q.append(mp[word])
                    v.add(mp[word])
        while q:
            r+=1
            for i in range(len(q)):
                n = q.popleft()
                if wordList[n] ==endWord:
                    return r
                for nei in adj[n]:
                    if nei not in v:
                        v.add(nei)
                        q.append(nei)
        return 0