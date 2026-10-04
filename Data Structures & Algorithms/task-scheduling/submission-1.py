
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        m = [-cnt for cnt in c.values()]
        heapq.heapify(m)
        t = 0
        q = deque()
        while m or q:
            t+=1
            if not m:
                t = q[0][1]
            else:
                cnt  = 1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,t+n])
            if q and q[0][1]==time:
                heapq.heappush(m,q.popleft()[0])
        return t
         