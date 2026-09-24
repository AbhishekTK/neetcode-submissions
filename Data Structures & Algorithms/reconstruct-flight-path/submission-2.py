class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        a = defaultdict(list)
        for s,d in sorted(tickets)[::-1]:
            a[s].append(d)
        
        r = []
        def d(s):
            while a[s]:
                dst = a[s].pop()
                d(dst)
            r.append(s)
            print(r)
        d("JFK")
        return r[::-1]
        
            