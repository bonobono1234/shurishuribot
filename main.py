import discord, datetime

client = discord.Client()

@client.event
async def on_ready(): 
    print("봇 준비완료!")
    print(client.user)

@client.event
async def on_message(message):
   
    if message.content == "^map":
        await message.channel.send("https://sheepfarm.io/map")       
   
    if message.content == "^medium":
        await message.channel.send("https://medium.com/@sheepfarm")       
    
    if message.content == "^guide":
        await message.channel.send("https://guide.sheepfarm.io/guide/")  

    if message.content == "^telegram":
        await message.channel.send("https://t.me/sheepmeta")    

    if message.content == "^twtter":
        await message.channel.send("https://twitter.com/SheepFarmMeta")     
    
    if message.content == "^로드맵":
        await message.channel.send("https://wre.notion.site/c38312b72f3d4e4c936c5788bde619ff")  
    
    if message.content == "^opensea":
        await message.channel.send("https://opensea.io/collection/sheepfarm")       
   
    if message.content == "^homepage":
        await message.channel.send("https://sheepfarm.io/")   
   
    if message.content == "^도움말":
        embed = discord.Embed(colour=discord.Colour.blue(), title="도움말", description="^map = 쉽팜 땅을 볼수있는 사이트를 전송합니다  ^medium = 쉽팜 미디움 사이트를 전송합니다  ^opensea = 쉽팜의 오픈씨 사이트를 전송합니다. ^twitter = 쉽팜의 트위터를 전송합니다 ^로드맵 = 쉽팜의 로드맵을 전송합니다  ^homepage = 쉽팜의 홈페이지를 전송합니다 ^로드맵 = 쉽팜의 로드맵을 전송합니다 ^내정보 = 내정보를 전송합니다 ^telegram = 쉽팜의 텔레그램을 전송합니다")
        await message.channel.send(embed=embed)
   
    if message.content == "^도와줘":
        await message.channel.send("당신을 도와드릴 수 없어요 ㅠㅠ")  
    
    if message.content == '^내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일은 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name}/{user.id}/{user.display_name}")
        await message.channel.send(message.author.avatar_url)
   
    if message.content.startswith("^청소"):
       number = int(message.content.split(" ")[1])
       if message.author.id == 762548751235285004:
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지 삭제 완료!")
       else:
           await message.delete()
           await message.channel.send("당신은 쭈니가 아닙니다!")
        access_token = os.environ['BOT_TOKEN']
client.run(access_token)

