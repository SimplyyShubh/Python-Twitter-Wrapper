from random import randrange
import time
import aiohttp
import asyncio

## Each request takes like 8-10 secs
async def getInfTweets():

    async with aiohttp.ClientSession() as session:
        r1 = "https://twitter-hype-backend.herokuapp.com/api/v1/users/"
        async with session.get(r1) as r:
            r1Usernames = await r.json()
        acc = len((r1Usernames)) - 1
        InfTweets = []

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
                continue
            username = r1Usernames[i]
            infTweet = "https://twitter.com/%s/status/%i" % (username, tweetId)
            InfTweets.append(infTweet)
            
    await session.close()
    return InfTweets

## print(asyncio.get_event_loop().run_until_complete(getInfTweets()))