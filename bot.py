import discord
from discord.ext import commands

from discord.ext.commands import cooldown
import random

client = commands.Bot(command_prefix = '+')



images =[
'https://media.discordapp.net/attachments/739021918593745007/742734769057693726/main-thumb-65769194-200-weqvbierzrfgtroalprddzxjrdvoavgm.jpeg',
'https://media.discordapp.net/attachments/739021918593745007/742775016461959269/20200803_085600.jpg']

images2 =[
'https://cdn.discordapp.com/attachments/739065079709827174/741583265508491264/Textonphoto20200808_142657.jpg']

images3 =[
'https://cdn.discordapp.com/attachments/739065079709827174/741368645678006312/-1148543461.png',
'https://cdn.discordapp.com/attachments/739021918593745007/742785303332520106/20200811_221320.jpg']

images4 =[
'https://cdn.discordapp.com/attachments/739065079709827174/739940433077207060/Screenshot_20200804-014741__01.jpg']

images5 =[
'https://cdn.discordapp.com/attachments/739065079709827174/741572230760104017/Textonphoto20200808_135252.jpg']

images6 = [
'https://cdn.discordapp.com/attachments/742788491980570634/742788764870508565/tenor-2.gif']


images7 =[
	'https://cdn.discordapp.com/attachments/742788525346521218/742788627104530432/d4b0b9f9-2c5b-420e-a82a-db1b50f49175.jpg'
]

images8 =[
	'https://cdn.discordapp.com/attachments/743067227544092724/743067294191845437/tenor.gif',
	'https://cdn.discordapp.com/attachments/743067227544092724/743067488069353563/tenor_1.gif',
	'https://cdn.discordapp.com/attachments/743067227544092724/743067952726933564/tenor_2.gif',
	
]
niceyarr = [
	'https://cdn.discordapp.com/attachments/743071873046151200/743076819020021860/tenor_3.gif',
	'https://cdn.discordapp.com/attachments/742723143873069106/743086527663439975/tenor.gif',
	'https://cdn.discordapp.com/attachments/742723143873069106/743086563856220250/tenor_1.gif'
]

dance = [
	'https://cdn.discordapp.com/attachments/743071873046151200/743090301790453860/tenor_3.gif'
]
@client.event
async def on_ready():
	await  client.change_presence(status=discord.Status.dnd, activity = discord.Game('FIFA'))
	
	print("bot is ready")




@client.event
@cooldown(1, 1000)  # 1000 second cooldown
async def comm(ctx):
    ...
    comm.reset_cooldown(ctx)


	



@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['hey','test'])
async def bolna(ctx, *,question):
	responses = ['yes bruh',
	              'nahhh',
	              'wth',
	              ]
	await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')



@client.command(aliases =['user' , 'info'])
async def xpose(ctx, member : discord.Member):
	embed = discord.Embed(titel = member.name , description = member.mention , color = discord.Colour.blue())
	embed.add_field(name = "ID", value = member.id , inline = True)
	embed.set_thumbnail(url = member.avatar_url)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed)





 
    


@client.command()
async def bajna(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'bajnaaaa', description =    f'{ctx.author.mention} **said bajna to** {member.mention}' , color = discord.Colour.blue())
	random_link = random.choice(images)
	embed.set_image(url = random_link)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed)
	await ctx.message.delete()





@client.command()
async def president(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'for president', description =    f'{ctx.author.mention} **choose** {member.mention}' , color = discord.Colour.blue())
	random_link2 = random.choice(images2)
	embed.set_image(url = random_link2)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed)
	await ctx.message.delete()






@client.command()
async def nai(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'NAI', description =    f'**nai** {member.mention}' , color = discord.Colour.blue())
	random_link3 = random.choice(images3)
	embed.set_image(url = random_link3)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed)
	await ctx.message.delete()



@client.command()
async def youthpower(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'YOUTH POWER', description =    f'**Youth power** {member.mention}' , color = discord.Colour.blue())
	random_link4 = random.choice(images4)
	embed.set_image(url = random_link4)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed)
	await ctx.message.delete()



@client.command()
async def yabebe(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'bebe', description =    f'**Ya bebe** {member.mention}' , color = discord.Colour.blue())
	random_link5 = random.choice(images5)
	embed.set_image(url = random_link5)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed)
	await ctx.message.delete()


@client.command()
async def modiji(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'hypocrisy', description =    f'**hypocrisy ki bhi seema hoti hai ** {member.mention} **ji**' , color = discord.Colour.blue())
	random_link6 = random.choice(images6)
	embed.set_image(url = random_link6)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed)
	await ctx.message.delete()




@client.command()
async def bhau(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'bhau nikal', description =    f'**nikal pheli fursat mai ** {member.mention}' , color = discord.Colour.blue())
	random_link6 = random.choice(images7)
	embed.set_image(url = random_link6)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed)
	await ctx.message.delete()



@client.command()
async def hug(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'hugs', description =    f'{ctx.author.mention} **hugs** {member.mention}' , color = discord.Colour.blue())
	random_link2 = random.choice(images8)
	embed.set_image(url = random_link2)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed)
	await ctx.message.delete()


@client.command()
async def nice(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'nice', description =    f'{ctx.author.mention} **said noice to** {member.mention}' , color = discord.Colour.blue())
	random_link8 = random.choice(niceyarr)
	embed.set_image(url = random_link8)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed )
	await ctx.message.delete()
	

@client.command()
async def cutedance(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'cutedance', description =    f'**cutie dance** {member.mention}' , color = discord.Colour.blue())
	random_link8 = random.choice(dance)
	embed.set_image(url = random_link8)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed )
	await ctx.message.delete()
	






client.run('NzQyMDE4MTQ3OTU5MzA4Mjg4.XzAAQA.-pE_bg5Owh_8SHnDfuNazVXI_b0')	
