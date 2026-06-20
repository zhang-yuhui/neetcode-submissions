class Twitter:

    def __init__(self):
        self.users = {}
        for i in range(101):
            self.users[i] = []
        self.follower = []
        for i in range(101):
            self.follower.append({i})
        self.stamp = 0
        s = set()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append((userId, tweetId, self.stamp))
        self.stamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        follower = self.follower[userId]
        post = []
        for i in follower:
            post += self.users[i]
        post.sort(key=lambda x:x[2], reverse=True)
        return [post[i][1] for i in range(min(10, len(post)))]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.follower[followerId].discard(followeeId)
