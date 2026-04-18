class Twitter:

    def __init__(self):
        self.followed_by_user = collections.defaultdict(set)
        self.most_recent_heap = []
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followed_by_user[userId].add(userId)
        heapq.heappush(self.most_recent_heap,[-self.time, tweetId, userId])
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        buffer = []
        news_feed = []
        while len(news_feed) < 10 and self.most_recent_heap:
            item = heapq.heappop(self.most_recent_heap)
            if item[2] in self.followed_by_user[userId]:
                 news_feed.append(item[1])
               
            buffer.append(item)
        
        for item in buffer:
            heapq.heappush(self.most_recent_heap, item)
        
        return news_feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed_by_user[followerId].add(followerId)
        self.followed_by_user[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
         self.followed_by_user[followerId].discard(followeeId)
