import discord
import random
from discord.ext import commands
from inshorts import inshorts
import config
client = commands.Bot(command_prefix='-tm', activity=discord.Activity(type=discord.ActivityType.listening, name="-tm"), status=discord.Status.online)

@client.event
async def on_ready():
    general_channel = client.get_channel(config.channel)
    await general_channel.send('Hello bois, Im online')

@client.event   
async def on_disconnect():
    general_channel = client.get_channel(config.channel)
    await general_channel.send('Bye uwus, Im going off')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-tm hello'):
        await message.channel.send('Hello uwu!')

    if message.content.startswith('-tm version'):
        myEmbed = discord.Embed(title="Cogent Bio", description="Compiling compelling global stories to impart cogent vision!", color= 0x0ff000)
        myEmbed.add_field(name="Current version",value="The bot version is 1.0",inline=False)
        myEmbed.add_field(name="Version code",value="v1.0.0",inline=False)
        myEmbed.add_field(name="Data Released:", value="24th June 2021", inline=False)
        myEmbed.add_field(name="Created by:", value="Suryaa_Seran//Sayf_Zakir_Hussain", inline=False)
        myEmbed.set_author(name="")
        await message.channel.send(embed=myEmbed)

    if message.content.startswith('-tm help'):
        text = "business,sports,world,politics,technology,startup,entertainment,miscellaneous,science,gossip,automobile"
        lines = text.split(",")
        for i in range(len(lines)):
            lines[i] = "*" + lines[i]
        text = "\n".join(lines)
        helpembed = discord.Embed(title="Cogent help", description="I got you mate", color= 0x0ff000)
        helpembed.add_field(name="Greet me",value="-tm hello",inline=False)
        helpembed.add_field(name="To get latest news",value="-tm news //category//",inline=False)
        helpembed.add_field(name="News Categories", value=text)
        helpembed.add_field(name="Know more about me",value="-tm version",inline=False)
        await message.channel.send('Aye I am a simple bot with simple needs')
        await message.channel.send(embed=helpembed)

    if message.content.startswith('-tm news'):
        cat =  message.content.split(' ')[2]
        news = inshorts(cat)
        if news.getNews()['success']:
            embeds = display(news)
            for x in embeds:
                await message.channel.send(embed=x)
        else:
            await message.channel.send('Bruhh take some help (-tm help). I cannot undertsand what you want.')


def display(news):
    res = news.getNews()
    stat = res['success']
    data = res['data']
    length = len(data)
    embeds= []
    num = random.sample(range(0, length-1), 3)
    for i in range (3):
        news_embed = discord.Embed(title=data[num[i]]['title'], description= data[num[i]]['content'], color= 0x0ff000)
        news_embed.set_image(url = data[num[i]]['imageUrl'])
        if data[num[i]]['readMoreUrl'] != None :
            news_embed.add_field(name="To know more",value= data[num[i]]['readMoreUrl'],inline=False)
        news_embed.add_field(name="Time",value= data[num[i]]['date'] + " " + data[num[i]]['time'], inline=False)
        news_embed.set_footer(text="Source: Inshorts")
        print(news_embed)
        embeds.append(news_embed)
    return embeds


client.run(config.api_key)

