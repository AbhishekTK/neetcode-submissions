class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        if len(self.tweetMap[userId])>10:
            self.tweetMap[userId].pop(0)
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        if len(self.followMap[userId])>=10:
            maxHeap= []
            for followeeId in self.folowMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId])-1
                    count , tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(maxHeap,[-count,tweetId,followeeId,index-1])
                    if len(maxHeap)>10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                c,t,f,i = heapq.heappop(maxHeap)
                heapq.heappush(minHeap,[-c,t,f,i])
        else:
            for f in self.followMap[userId]:
                if f in self.tweetMap:
                    i = len(self.tweetMap[f])-1
                    c,t = self.tweetMap[f][i]
                    heapq.heappush(minHeap,[c,t,f,i-1])
            while minHeap and len(res)<10:
                c,t,f,i = heapq.heappop(minHeap)
                res.append(t)
                if i>=0:
                    c,t = self.tweetMap[f][i]
                    heapq.heappush(minHeap,[c,t,f,i-1])
            return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
