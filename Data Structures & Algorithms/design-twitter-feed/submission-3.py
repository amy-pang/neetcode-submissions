class Twitter:

    def __init__(self):
        self.count = 0  # negative for maxHeap
        self.tweets = defaultdict(list)    # userID, list of -count, tweetID
        self.following = defaultdict(set) # userID, set of following


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        topTen = []
        maxHeap = []
        self.following[userId].add(userId)
        # make maxHeap
        for followeeId in self.following[userId]:
            for t in self.tweets[followeeId]:
                heapq.heappush(maxHeap, t)
        i = 0
        while maxHeap and i < 10:
            topTen.append(heapq.heappop(maxHeap)[1])
            i += 1
        
        return topTen
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
