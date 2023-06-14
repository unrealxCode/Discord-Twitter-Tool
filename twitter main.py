import tweepy
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.command()
async def farm(ctx, tweet_id):
        
    client = tweepy.Client(consumer_key='',
                       consumer_secret='',
                       access_token='',
                       access_token_secret='')

    client.create_tweet(text='retweet reply', in_reply_to_tweet_id=tweet_id)

    await ctx.send('Reply sent to tweet with ID: ' + tweet_id)

#token
client.run('')
