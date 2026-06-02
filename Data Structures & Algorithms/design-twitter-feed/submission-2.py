class Twitter:

    def __init__(self):
        self.userfol = dict()
        self.userposts = dict()
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userfol:
            self.userfol[userId] = [userId]

        if userId not in self.userposts:
            self.userposts[userId] = [(self.time,tweetId)]
        else:    
            self.userposts[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.userfol:
            return []
        allposts = []

        for user in self.userfol[userId]:
            if user in self.userposts:
                allposts = allposts + self.userposts[user][-10:]

        allposts.sort(reverse=True)
        arr = []

        for post in allposts[:10]:
            arr.append(post[1])
        return arr

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userfol:
            self.userfol[followerId] = [followerId,followeeId]
        else:
            if followeeId not in self.userfol[followerId]:
                self.userfol[followerId].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.userfol:
            self.userfol[followerId] = [followerId]
        else:
            if followeeId in self.userfol[followerId]:
                self.userfol[followerId].remove(followeeId)
        
