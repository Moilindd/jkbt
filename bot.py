

import base64
import json
import os
import random
from random import randint
import re
import signal
import sys
import urllib.parse
import datetime
import imagetools
import utils
from resizeimage import resizeimage
import fonts
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import requests
import praw




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
'https://cdn.discordapp.com/attachments/739021918593745007/743822883184443402/-1148543461.png',
'https://cdn.discordapp.com/attachments/739021918593745007/743822848036175972/20200811_221320.jpg']

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



fuckofff = [
	'https://cdn.discordapp.com/attachments/743067227544092724/743382141378887721/de7fe5a74875311b05346aba8e534168.gif',
	'https://cdn.discordapp.com/attachments/743067227544092724/743408172999639080/tumblr_n9wt7ukcGX1sqqwsuo1_500.gif',
	'https://cdn.discordapp.com/attachments/743067227544092724/743408173381058620/fuck_off_ryan_stiles.gif'
]
enc =[
  'https://cdn.discordapp.com/attachments/746868628292632627/768479860620263464/sct42nk8_vikas-dubey_295x200_09_July_20.png',
  'https://cdn.discordapp.com/attachments/746868628292632627/768493271679762442/e91d7758f43a056636313cead62ba572.png',
  'https://cdn.discordapp.com/attachments/746868628292632627/768481781477015562/adityanath-1.png',
  'https://cdn.discordapp.com/attachments/746868628292632627/768482685646929942/yogi-aditiyanath1-08-1491625317-1542696237.jpg'
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
	              'dude chill',
                'get a life',
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
async def say(ctx,*,msg):
   
       await ctx.send("{}" .format(msg))


 
    


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
	


@client.command()
async def fuckoff(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'fuckoff', description =    f'**fuck off** {member.mention}' , color = discord.Colour.blue())
	random_link9 = random.choice(fuckofff)
	embed.set_image(url = random_link9)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed )
	await ctx.message.delete()
	

@client.command()
async def encounter(ctx, member : discord.Member):
	embed = discord.Embed(titel = 'encounter', description =    f'**Badtameezi mat karo varna gaadi palatwa denge** {member.mention}' , color = discord.Colour.blue())
	random_link9 = random.choice(enc)
	embed.set_image(url = random_link9)
	embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")
	await ctx.send (embed=embed )
	await ctx.message.delete()
	































@client.command(helpinfo='Wikipedia summary', aliases=['w', 'wiki'])
async def wikipedia(ctx, *, query: str):
    '''
    Uses Wikipedia APIs to summarise search
    '''
    sea = requests.get(
        ('https://en.wikipedia.org//w/api.php?action=query'
         '&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop='
        ).format(query)).json()['query']

    if sea['searchinfo']['totalhits'] == 0:
        await ctx.send('Sorry, your search could not be found.')
    else:
        for x in range(len(sea['search'])):
            article = sea['search'][x]['title']
            req = requests.get('https://en.wikipedia.org//w/api.php?action=query'
                               '&utf8=1&redirects&format=json&prop=info|images'
                               '&inprop=url&titles={}'.format(article)).json()['query']['pages']
            if str(list(req)[0]) != "-1":
                break
        else:
            await ctx.send('Sorry, your search could not be found.')
            return
        article = req[list(req)[0]]['title']
        arturl = req[list(req)[0]]['fullurl']
        artdesc = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/'+article).json()['extract']
        lastedited = datetime.datetime.strptime(req[list(req)[0]]['touched'], "%Y-%m-%dT%H:%M:%SZ")
        embed = discord.Embed(title='**'+article+'**', url=arturl, description=artdesc, color=0x3FCAFF)
        embed.set_footer(text='Wiki entry last modified',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.set_author(name='Wikipedia', url='https://en.wikipedia.org/',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.timestamp = lastedited
        await ctx.send('**Search result for:** ***"{}"***:'.format(query), embed=embed)



hearts = ['❤', '💛', '💚', '💙', '💜']

@client.command()
async def pressF( ctx , text: commands.clean_content = None):
     """ Press F to pay respect """
     reason = f"for **{text}** " if text else ""
     await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")
     



@client.command(aliases=['howsoft', 'soft'])
async def softiecalc( ctx, user: discord.Member = None):
        """ Returns a random percent for how softie is a discord user """
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "<:baj:754937908330233907>"
        if hot > 25:
            emoji ="<:baj:754937908330233907>"
        if hot > 50:
            emoji = "<:soft:754938140862447647>"
        if hot > 75:
            emoji = "<:soft:754938140862447647>"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** soft {emoji}")


@client.command(aliases=['tf'])
async def textface(ctx,Type:commands.clean_content = None):
        """Get those dank/cool faces here. Type prefix textface list for a list."""
        if Type is None:
            await ctx.send('That is NOT one of the dank textfaces in here yet. Use: prefix textface [lenny/tableflip/shrug]')
        else:
            if Type.lower() == 'lenny':
              await ctx.send('( ͡° ͜ʖ ͡°)')
            elif Type.lower() == 'tableflip':
              await ctx.send('(ノಠ益ಠ)ノ彡┻━┻')
            elif Type.lower() == 'shrug':
              await ctx.send('¯\_(ツ)_/¯')
            elif Type.lower() == 'bignose':
              await ctx.send('(͡ ͡° ͜ つ ͡͡°)')
            elif Type.lower() == 'iwant':
              await ctx.send('ლ(´ڡ`ლ)')
            elif Type.lower() == 'musicdude':
              await ctx.send('ヾ⌐*_*ノ♪')
            elif Type.lower() == 'wot':
              await ctx.send('ლ,ᔑ•ﺪ͟͠•ᔐ.ლ')
            elif Type.lower() == 'bomb':
              await ctx.send('(´・ω・)っ由')
            elif Type.lower() == 'orlly':
              await ctx.send("﴾͡๏̯͡๏﴿ O'RLY?")
            elif Type.lower() == 'money':
              await ctx.send('[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]')
            elif Type.lower() == 'list':
              color = discord.Color(value=0x00ff00)
              em = discord.Embed(color=color, title='List of Textfaces')
              em.description = 'Choose from the following: lenny, tableflip, shrug, bignose, iwant, musicdude, wot, bomb, orlly, money. Type prefix textface [face].'
              em.set_footer(text="Don't you dare question my names for the textfaces.")
              await ctx.send(embed=em)
            else:
              await ctx.send('That is NOT one of the dank textfaces in here yet. Use prefix textface list to see a list of the textfaces.')

			  

@client.command()
async def trigger(ctx, member:discord.Member=None):
        """Triggers a user"""
        await ctx.channel.trigger_typing()
        if member is None:
            member = ctx.author
        await member.avatar_url.save("trigger.png")
        avatar = Image.open("trigger.png")
        triggered = resizeimage.resize_cover(Image.open("pillow/triggered.jpg"), [769,100])
        position = 0, avatar.getbbox()[3] - triggered.getbbox()[3]
        avatar.paste(triggered, position)
        avatar.save("trigger.png")
        await ctx.send(file=discord.File("trigger.png"))



@client.command()
async def blackandwhite(ctx, user:discord.Member=None):
        """Turns your avatar or the specified user's avatar black and white"""
        await ctx.channel.trigger_typing()
        if user is None:
            user = ctx.author
        await user.avatar_url.save("blackandwhite.png")
        avatar = Image.open("blackandwhite.png").convert("L")
        avatar.save("blackandwhite.png")
        await ctx.send(file=discord.File("blackandwhite.png")) 

@client.command(aliases=['sr', 'simp'])
async def simprate( ctx, user: discord.Member = None):
        user = user or ctx.author
        
        

        
        r = random.randint(1, 100)
        hot = r / 1.001

        emoji = "  (ᇴ‿ฺᇴ)"
        if hot > 25:
            emoji =" (ᇴ‿ฺᇴ)"
        if hot > 50:
            emoji = "๐·°(৹˃̵﹏˂̵৹)°·๐ **Welcome to SIMP gang**"
        if hot > 75:
            emoji = "๐·°(৹˃̵﹏˂̵৹)°·๐ **Welcome to SIMP gang**"
           
        await ctx.send(f"**{user.name}** is **{hot:.2f}%** simp {emoji}")
@client.command()
async def meme(ctx):
    reddit =praw.Reddit(client_id="IWcUAuvid2Awiw",
                     client_secret="bnGXw_QH7Tt24dtyw-kHi6WUmaA",
                     password="OKAYcool123",
                     user_agent="testscript by /u/fakebot3",
                     username="moilinddd",
                    redirect_uri="http://localhost:8080",)

    meme_subreddits =["dankmemes","im14andthisisdeep","terriblefacebookmemes","PewdiepieSubmissions","teenagers","MemeEconomy"]
    reg_img =  r".*/(i)\.redd\.it"

    async with ctx.typing():
            selected_subreddit = meme_subreddits[randint(0, len(meme_subreddits) - 1)]
            memes_submissions = reddit.subreddit(selected_subreddit).hot()
            post_to_pick = randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            if submission.over_18:
                return
            embed = discord.Embed(
                title=f"r/{selected_subreddit} " + f"- {submission.title}",
                colour=discord.Colour(0xFF4500),
            )
            embed.set_author(
                name="Reddit",
                icon_url="https://www.redditstatic.com/desktop2x/"
                + "img/favicon/android-icon-192x192.png",
            )
            match = re.search(reg_img, submission.url)
            embed.add_field(name="Upvotes", value=submission.score)
            embed.add_field(name="Comments", value=submission.num_comments)
            if match:
                embed.set_image(url=submission.url)
            else:
                await ctx.send(embed=embed)
                await ctx.send(submission.url)
                return
            await ctx.send(embed=embed)	  

@client.command(aliases = ['ship','lovecalc'])
async def lc(ctx, name_one: discord.Member, name_two: discord.Member):
        love_meter = (name_one.id + name_two.id) % 100
       
        if love_meter >= 95:
            love_status = LOVE_STAT['95'][randint(0, len(LOVE_STAT['95']))]
            love_stat_i = '95'
            emote = "<a:700833891161997443:769832299424382987>"
        elif 80 <= love_meter < 90:
           emote = "<a:700833891161997443:769832299424382987>"
            
        elif 60 <= love_meter < 80:
            emote = "<a:700833891161997443:769832299424382987>"
            love_stat_i = '60'
        elif 45 <= love_meter < 60:
            emote = "<a:700833891161997443:769832299424382987>"
            love_stat_i = '45'
        elif 30 <= love_meter < 45:
            emote = "<a:700833891161997443:769832299424382987>"
            love_stat_i = '30'
        elif 20 <= love_meter < 30:
            emote = "<a:700833891161997443:769832299424382987>"
            love_stat_i = '20'
        elif 5 <= love_meter < 20:
           emote = "<a:700833891161997443:769832299424382987>"
            
        elif 1 <= love_meter < 5:
           emote = "<a:700833891161997443:769832299424382987>"
            
        else:
            love_meter = 100
            emote = "<a:700833891161997443:769832299424382987>"
            love_stat_i = '0'

        embed = discord.Embed(
            title=f"Kundali mila rahe ruko jara! {emote}",
            description=f'**{name_one.display_name}** \u2764 **{name_two.display_name}** scored {love_meter}%!\n\u200b',
            color=discord.Color.dark_magenta()
        )
        embed.set_author(
            name='From : Seema Aunty(Matchmaker)'

        )
        embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}")  

         

        await ctx.message.channel.send(embed=embed)







client.run('**************')	
