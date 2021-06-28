import os
import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio

prefix = os.getenv("PREFIX")
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Help AutoOwO", color=420699, description=f"**{prefix}autoOwO**\nowoh, owo sell all, owo flip 500 and owo cash 50 seconds.\n\n**{prefix}stopautoOwO**\nstops autoOwO.")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/858922949452103710/858928737746812988/44240a043c5e0ee4d3d7cb70ce42b77e.gif")
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def autoOwO(ctx):
	await ctx.message.delete()
	await ctx.send('auto OwO is now **enabled**!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send('owoh')
			print(f"{Fore.GREEN}succefully owoh")
			await asyncio.sleep(15)
			await ctx.send('owo sell all')
			print(f"{Fore.GREEN}succefully sell")
			await ctx.send('owo flip 500')
			print(f"{Fore.GREEN}succefully owo flip 500")
			await asyncio.sleep(10)
			await ctx.send('owo cash')
			print(f"{Fore.GREEN}succefully cash")
			await asyncio.sleep(10)


@bot.command()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send('auto OwO is now **disabled**!')
	global dmcs
	dmcs = False

@bot.event
async def on_ready():
  activity = discord.Game(name="^_^", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f'''{Fore.RED}
😾♕  ρŘＡ几ᵃＶ  ♡😲

{Fore.GREEN}
🄰🅄🅃🄾🄾🅆🄾
selfbot is ready!
''')

bot.run(token, bot=False)
