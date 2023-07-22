import asyncio, discord, time 
from discord.ext import commands
import requests
import json
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
token = open("token.txt", "r").readline()

@bot.event
async def on_ready():
    print("I have logged in as {0.user}\n".format(bot))

@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕")

@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(title = "채널 아이앤 도우미", description = "This is not hacking ~!", color = 0x6E17E3) 
    embed.add_field(name = bot.command_prefix + "도움말", value = "도움말을 봅니다", inline = False)
    embed.add_field(name = bot.command_prefix + "mint 지갑주소 토큰아이디 민팅갯수", value = "채널아이앤 지정 nft를 민팅함 (관리자 api 호출)", inline = False)
    await ctx.send(embed=embed)

@bot.command()
async def mint(ctx, address, tokenid, count):
  url = "https://admin.channel-in.io:5000/nfts/mint/daily"
  response = requests.get(url)

  payload = json.dumps({
  "address": address,
  "tokenId": tokenid,
  "count": count
  })
  headers = {
  'sec-ch-ua-platform': '"Windows"',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ko,en;q=0.9,en-US;q=0.8',
  'Content-Length': '109',
  'Content-Type': 'application/json',
  'Origin': 'https://channel-in.io',
  'Referer': 'https://channel-in.io/',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
  'sec-ch-ua-mobile': '?0',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjYzZTBhOTk1YjRkMmUyMjA5ZTQ5MzE4MyJ9.eyJ0eXAiOiJhY2Nlc3MiLCJfaWQiOiI2M2UwYTk5NWI0ZDJlMjIwOWU0OTMxODMiLCJuYW1lIjoiYWRtaW5Qcm92aWRlciIsImxldmVsIjoxLCJjcmVhdGVkQXQiOiIyMDIzLTAyLTA2VDA3OjE3OjQxLjU4MFoiLCJ1cGRhdGVkQXQiOiIyMDIzLTAyLTA2VDA3OjE3OjQxLjU4MFoiLCJpZHgiOjEsImlhdCI6MTY3NTc1Njk4OCwiZXhwIjozMDgyOTU5ODc2ODY4MiwiYXVkIjpbImJ0OmFkbWluIiwiYnQ6YXBpIiwiYnQ6dXNlciIsImNpOmFkbWluIiwiY2k6YXBpIiwiY2k6dXNlciIsImttOmFkbWluIiwia206YXBpIiwia206dXNlciIsIm9yOmFkbWluIiwib3I6YXBpIiwib3I6dXNlciIsInBmOmFkbWluIiwicGY6YXBpIiwicGY6dXNlciIsInBwOmFkbWluIiwicHA6YXBpIiwicHA6dXNlciJdLCJpc3MiOiJjaWNfZGV2ZWxvcGVycyIsInN1YiI6ImFjY2Vzc190b2tlbl9zaG9ydGVyIiwianRpIjoiMSJ9.vCWTeBeJ715jaM_ussAprpvu3TMMqIrfXbb1PfpXVm8'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  print(response)
  print(response.text)
  if response.text == "0":
    await ctx.send("nft 민팅성공!")
  else:
     await ctx.send("nft 민팅실패 다시 시도해보세요.")

bot.run(token)
