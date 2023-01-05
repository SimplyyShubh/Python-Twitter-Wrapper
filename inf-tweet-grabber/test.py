import requests
from random import randrange
import time
import aiohttp
import asyncio

## Each request takes like 10 secs
async def getInfTweets():

    r1 = "https://twitter-hype-backend.herokuapp.com/api/v1/users/"
    r = requests.get(url = r1)
    r1Usernames = r.json()
    acc = len((r.json())) - 1
    InfTweets = []

    async with aiohttp.ClientSession() as session:

        for i in range (0, int(acc)):
            r2 = "https://twitter-hype-backend.herokuapp.com/api/v1/accounts/%i" % (i)
            async with session.get(r2) as tweet:
                tweetData = await tweet.json()
            # r3 = "https://twitter-hype-backend.herokuapp.com/api/v1/users/%i" % (i)
            # async with session.get(r3) as users:
            #     username = await users.json()
            randomInt = randrange(4)
            try:
                tweetId = int(tweetData["data"][randomInt]["id"])
            except:
                i = i + 1
                r2 = "https://twitter-hype-backend.herokuapp.com/api/v1/accounts/%i" % (i)
                async with session.get(r2) as tweet:
                    tweetData = await tweet.json()
                # r3 = "https://twitter-hype-backend.herokuapp.com/api/v1/users/%i" % (i)
                # async with session.get(r3) as users:
                #     username = await users.json()
                randomInt = randrange(4)
                tweetId = int(tweetData["data"][randomInt]["id"])

            username = r1Usernames[i]
            infTweet = "https://twitter.com/%s/status/%i" % (username, tweetId)
            InfTweets.append(infTweet)
            
    await session.close()
    return InfTweets