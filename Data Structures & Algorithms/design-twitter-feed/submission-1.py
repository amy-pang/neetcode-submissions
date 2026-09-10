class Twitter:

    def __init__(self):
        self.tweets = []    # userID, tweetID
        self.following = defaultdict(set) # userID, set of following


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        topTen = []
        for i in range(len(self.tweets) - 1, -1, -1):
            tweetUserId = self.tweets[i][0]
            tweetId = self.tweets[i][1]
            if tweetUserId == userId or tweetUserId in self.following[userId]:
                topTen.append(tweetId)
            if len(topTen) == 10:
                break
        
        return topTen
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
