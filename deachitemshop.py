import tweepy
import time
import os
import subprocess
import requests
import PIL
import datetime
import json
from datetime import date
from PIL import Image
import discord
from discord.ext import commands, tasks
from config import settings

today = date.today()

# Program title :)
os.system("cls")
os.system(
    "TITLE FortniteTweetPoster / By Fevers")

# Grabs current date, and puts it into Month, Day, Year
d2 = today.strftime("%B %d, %Y")
print("\nCurrent date:", d2)

# -----------------------------------------------------------------------------------------#

#  Put your Twitter API keys, username, and SAC here!

twitAPIKey = 'XXXXXX'
twitAPISecretKey = 'XXXXXX'
twitAccessToken = 'XXXXXX'
twitAccessTokenSecret = 'XXXXXX'
username = 'revolex'
sac = 'DeachOpOp'

# Item Shop Config - leave both configs the same for default. Background urls are NOT supported.

textcolor = 'ffffff'
backgroundcolor = '1F1F1F'

# https://fortniteapi.io API key goes here (ONLY REPLACE THE XXXX PART):

apikey = 'af17b1e9-31ed87dd-c3c75197-4b4d5108'
# -----------------------------------------------------------------------------------------#

# Grabs twitter api keys from settings
auth = tweepy.OAuthHandler(twitAPIKey, twitAPISecretKey)
auth.set_access_token(twitAccessToken, twitAccessTokenSecret)
api = tweepy.API(auth)

headers = {'Authorization': apikey}

# ------------------
response = requests.get('https://pastebin.com/raw/i6UiYQX8')
print('\n------------')
print('Current updates:')
ln1 = response.json()["1"]
ln2 = response.json()["2"]
ln3 = response.json()["3"]
seasonend = response.json()["seasonend"]
currentseason = response.json()["currentseason"]
latestVersion = response.json()["currentVersion"]
leaksimage = response.json()['leaksurl']
print("")
print("")
print(ln1)
print(ln2)
print('------------')
# ------------------

parsedseasonend = seasonend.split(", ")

seasoncountdown = datetime.date(int(parsedseasonend[0]), int(parsedseasonend[1]),
                                int(parsedseasonend[2])) - datetime.date.today()

seasoncountdown = str(seasoncountdown)

print('----------------------------------------------')
print("Supported lines:\n\n")
print('shop = Posts Item Shop')
print('----------------------------------------------\n')

# If user wants to post the shop, then....
def createItemShop():
    print("Running shop for", username)
    url = 'https://api.nitestats.com/v1/shop/image?footer=Creator%20Code%3A%20' + str(sac) + '&textcolor=' + str(
        textcolor) + '&background=' + str(backgroundcolor)
    r = requests.get(url, allow_redirects=True)
    open('shop.png', 'wb').write(r.content)
    print("\nOpened shop.png")
    print("\nSaved shop.png")
    print('Now closing program.')






if __name__ == '__main__':
    createItemShop()

    TOKEN = 'ODM3Mzc1ODk5ODU4NjMyODE0.YIrpFA.n0uvvqHFx_Rr00gVd4HF9Rnmrbg'
    bot = commands.Bot(command_prefix='!')


    @bot.command(pass_context=True)  # разрешаем передавать агрументы
    async def test(ctx):  # создаем асинхронную фунцию бота
        await ctx.send('Пошел нахуй')  # отправляем обратно аргумент

    @bot.command()
    async def huy(gg):
        await gg.send('мать трахал')
    @bot.command()
    async def itemshop(shop):
        await shop.send('Магазин на: ' + d2)
        await shop.send('Используй тег автора **DeachOpOp** при покупке товаров в магазине предметов!', file=discord.File('shop.png'))
        await shop.send('Кидай скрины в канал чтобы получить специальную роль.')
        await shop.send('С этой ролью ты сможешь играть со стримером **вне очереди**!')


    @bot.event
    async def on_ready():
        change_status.start()
        print('bot in active')

    @tasks.loop(seconds=3600)
    async def change_status():
        channel = bot.get_channel(638652839689846795)
        print('sended!')
        await channel.send('Магазин на: ' + d2 + ' ✨')
        x = await channel.send('Используй тег автора **DeachOpOp** при покупке товаров в магазине предметов! 🥰',
                        file=discord.File('shop.png'))
        await x.add_reaction(emoji="👍")
        await x.add_reaction(emoji="👎")
        await channel.send('Кидай скрины в канал чтобы получить специальную роль. ✔️')
        await channel.send('С этой ролью ты сможешь играть со стримером **вне очереди**! 🔥')



    bot.run(TOKEN)
# appid 837375899858632814
# publickey 25e2ceb8aa5d954aeeb2ced3f9b0ff205c98ab1382f92e90655ec6902d9deceb
# clientsecret A4dfN153u0zh923SeXRyoabResxLs6AX
# token ODM3Mzc1ODk5ODU4NjMyODE0.YIrpFA.n0uvvqHFx_Rr00gVd4HF9Rnmrbg
