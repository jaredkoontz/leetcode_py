import heapq
from collections import defaultdict

import pytest


"""
each user needs to be able to view a random viewers posts, which indicates fast retrival so a hash map will
store users

each user needs to have a list of tweets.
these tweets need to preserve order by when it was tweeted by a user.

this indicates a linked list or heap for keeping order. I am going to go with a heap just cause its ez pz
in python
"""


class Tweets:
    def __init__(self):
        self.tweets = []

    def add(self, tweet_id):
        # maintain 10 tweets here?
        curr_len = len(self.tweets)
        heapq.heappush(self.tweets, (curr_len, tweet_id))

    def as_list(self):
        return self.tweets


class User:
    def __init__(self, user_id, tweets):
        self.user_id = user_id
        self.tweets = tweets
        self.followed = set()


class UserFactory:
    @staticmethod
    def create_user(user_id):
        return User(user_id, Tweets())


class Users:
    def __init__(self):
        self.users = {}

    def _get_user_or_add(self, user_id) -> User:
        if user_id in self.users:
            return self.users[user_id]
        else:
            return UserFactory.create_user(user_id)

    def get_users_tweets(self, user_id: int) -> list[int]:
        if user_id in self.users:
            return self.users[user_id].as_list()

        else:
            return []

    def add_tweet(self, user_id: int, tweet_id: int):
        user = self._get_user_or_add(user_id)
        user.tweets.add(tweet_id)

    def follow(self, follower_id, followee_id):
        follower = self._get_user_or_add(follower_id)
        followee = self._get_user_or_add(followee_id)

        follower.followed.add(followee)

    def unfollow(self, follower_id, followee_id):
        follower = self._get_user_or_add(follower_id)
        followee = self._get_user_or_add(followee_id)
        try:
            follower.followed.remove(followee)
        except KeyError:
            # do we care? not really, is idempotent
            pass

    def get_news_feed(self, user_id: int) -> list[int]:
        #
        pass


class CppTwitter:
    def __init__(self):
        self.follower = defaultdict(set)
        self.tweetmap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetmap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        result = []
        pq = []

        # Add user's own tweets
        for time, tweetId in self.tweetmap.get(userId, []):
            heapq.heappush(pq, (-time, tweetId))

        # Add tweets from people they follow
        for followeeId in self.follower.get(userId, []):
            for time, tweetId in self.tweetmap.get(followeeId, []):
                heapq.heappush(pq, (-time, tweetId))

        # Get top 10 most recent tweets
        for _ in range(10):
            if pq:
                result.append(heapq.heappop(pq)[1])
            else:
                break

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)


class TheirTwitter:
    def __init__(self):
        self.timestamp = 0
        self.user_tweets = {}
        self.user_follows = {}

    def postTweet(self, userId, tweetId):
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.timestamp += 1
        self.user_tweets[userId].append((-self.timestamp, tweetId))

    def getNewsFeed(self, userId):
        heap = []
        if userId in self.user_tweets:
            heap.extend(self.user_tweets[userId][-10:])
        if userId in self.user_follows:
            for followeeId in self.user_follows[userId]:
                if followeeId in self.user_tweets:
                    heap.extend(self.user_tweets[followeeId][-10:])
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])
        return feed

    def follow(self, followerId, followeeId):
        if followerId not in self.user_follows:
            self.user_follows[followerId] = set()
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if (
            followerId in self.user_follows
            and followeeId in self.user_follows[followerId]
        ):
            self.user_follows[followerId].remove(followeeId)


class MyTwitter:
    def __init__(self):
        self.users = Users()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users.add_tweet(userId, tweetId)

    def getNewsFeed(self, userId: int) -> list[int]:
        return self.users.get_news_feed(userId)

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users.follow(followerId, followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users.unfollow(followerId, followeeId)


Twitter = CppTwitter


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
            [
                "Twitter",
                "postTweet",
                "getNewsFeed",
                "follow",
                "postTweet",
                "getNewsFeed",
                "unfollow",
                "getNewsFeed",
            ],
            [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]],
            [None, None, [5], None, None, [6, 5], None, [5]],
        ),
    ],
)
def test_design_twitter_cache(operations, init, expected):
    twitter = None
    for op, components, curr_val in zip(operations, init, expected):
        if op == "Twitter":
            twitter = Twitter()
        elif op == "postTweet":
            assert twitter.postTweet(components[0], components[1]) == curr_val
        elif op == "getNewsFeed":
            assert twitter.getNewsFeed(components[0]) == curr_val
        elif op == "follow":
            assert twitter.follow(components[0], components[1]) == curr_val
        elif op == "unfollow":
            assert twitter.unfollow(components[0], components[1]) == curr_val
        else:
            raise NotImplementedError
