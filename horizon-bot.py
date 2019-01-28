import discord
import asyncio
from discord.utils import get
import random


#VARIABLES. DO NOT CHANGE!!!!#

#removed server specific data#
TOKEN = "TOKEN_GOES_HERE"


#END OF VARIABLES#
client = discord.Client()

#boot and set game
@client.event
async def on_ready():
    print("Bot is G2G!")
    game = discord.Game("Doing bot things")
    await client.change_presence (status = discord.Status.online, activity = game)

#react to messages that include these emojis for the memes
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    channel = message.channel
    if message.author == client.user:
        return
    if ':ste:' in message.content:
        await message.add_reaction("ste:507910573598441472")
    if ':dan:' in message.content:
        await message.add_reaction("dan:507916045818920960")
    if ':matty:' in message.content:
        await message.add_reaction("matty:507918013224321036")
    if ':al:' in message.content:
        await message.add_reaction("al:507912964578344960")
    if message.content.startswith("-h"):
        if message.author == client.user:
            return
        if 'help' in message.content:
            await channel.send("```HORIZON BOT COMMANDS:\n  * -h commands - A list of commands\n  * -h info - Information about the bot\n * -h schedule - Posts the clubs schedule\n * -h twitch - Get the Horizon Twitch link\n * -h status - Yep, you guessed it. Get the status\n * -h price - Run down of prices of stuff at Horizon\n * -h MFGC - Info on Fighting Games at Horizon and the best people to talk to about it\n * -h membership - Info on membership at Horizon\n * -h 1v1 (and put the username)```")
        elif 'info' in message.content:
            await channel.send("```This bot was made by Dan, cos he's a fuckin' beast and got really bored.```")
        elif 'schedule' in message.content:
            await channel.send("```MONDAY - League of Legends\nTUESDAY - Overwatch\nWEDNESDAY - 2-4-1 on packages\nTHURSDAY - Fighting Games with Merseyside Fighting Game Community & DOTA2\nFRIDAY - Fortnite\nSATURDAY - Black Ops 4\nSUNDAY - Fighting Games with Merseyside Fighting Game Community 2-4-1 on packages\n\nAll clubs are £10 for 3-10, you can arrive after 3 (you still save money if you get here before 8!!). Fighting games cost £2 and runs from 3-10 in the cafe area - BRING YOUR STICKS!\n```")
        elif 'twitch' in message.content:
            await channel.send("```https://www.twitch.tv/horizonliverpool```")
        elif 'status' in message.content:
            await channel.send("```I have a boyfriend, sorry.```")
        elif '1v1' in message.content:
            slicedMessage = str(message.content)
            await channel.send("```" + str(message.author.nick) + " has challenged" + slicedMessage.replace("-h 1v1", " ") + "to a 1v1.```")
            await channel.send("```***   FIGHTING   ***```")
            await asyncio.sleep(2)
            await channel.send("```***   FIGHTING   ***```")
            await asyncio.sleep(2)
            await channel.send("```***   DUST SETTLING   ***```")
            await channel.send("```***   AND THE WINNER IS   ***```")
            await asyncio.sleep(3)
            num = random.randint(1,20)
            if num >= 1 and num <= 10:
                await channel.send("```***   " + str(message.author.nick) + "    ***```")
            else:
                await channel.send("```***   " + slicedMessage.replace("-h 1v1", " ") + "    ***```")
        elif 'prices' in message.content:
            await channel.send("```GUESTS - £5.99 per hour\nMEMBERS - £3.99 per hour\n*PACAKAGES*\n  - 3 hours & drink - £15\n  - 5 hours & drink - £20\n  - 2-4-1 on these packages Wednesday & Sunday\n```")
        elif 'MFGC' in message.content:
            await channel.send("```If you love knocking 7 shades of shit out of your mates, or complete strangers come to Horizon on Thursday or Sunday, 3pm onwards for Fighting Games Club hosted by Merseyside Fighting Game Community.\nJoin their Discord server here: https://discord.gg/Qz8TbaV```")
        elif 'membership' in message.content:
            await channel.send("```Top up £50, or £30 for students, and get a Horizon Membership card. The money is yours to spend from your account on PC time/food/drinks etc. we don't charge for the membership.```")
        else:
            await channel.send("```No command found, use -h help for a list of available commands.```")

@client.event
async def on_reaction_add(reaction, member):
    #removed server specific data#
    welcomeChannelID = CHANNEL_ID_GOES_HERE
    if reaction.message.channel.id == welcomeChannelID:
        BlackOps4 = discord.utils.get(member.guild.roles, name='BlackOps4')
        Fortnite = discord.utils.get(member.guild.roles, name='Fortnite')
        CSGO = discord.utils.get(member.guild.roles, name='CS:GO')
        League = discord.utils.get(member.guild.roles, name='League')
        DOTA = discord.utils.get(member.guild.roles, name='DOTA2')
        Overwatch = discord.utils.get(member.guild.roles, name='Overwatch')
        PUBG = discord.utils.get(member.guild.roles, name='PUBG')
        RocketLeague = discord.utils.get(member.guild.roles, name='RocketLeague')
        AllGames = discord.utils.get(member.guild.roles, name='AllGames')
        FightingGames = discord.utils.get(member.guild.roles, name='FightingGames')   
        if str(reaction.emoji) == "<:bo4:510614885336350742>":
            await member.add_roles(BlackOps4, atomic = True)
        if str(reaction.emoji) == "<:fortnite:510614994283528193>":
            await member.add_roles(Fortnite, atomic = True)
        if str(reaction.emoji) == "<:csgo:510615696162422794>":
            await member.add_roles(CSGO, atomic = True)
        if str(reaction.emoji) == "<:league:510615023836725248>":
            await member.add_roles(League, atomic = True)
        if str(reaction.emoji) == "<:dota:510614956358500352>":
            await member.add_roles(DOTA, atomic = True)
        if str(reaction.emoji) == "<:overwatch:510615060276707348>":
            await member.add_roles(Overwatch, atomic = True)
        if str(reaction.emoji) == "<:pubg:510615088655368193>":
            await member.add_roles(PUBG, atomic = True)
        if str(reaction.emoji) == "<:rocketleague:510615116002230290>":
            await member.add_roles(RocketLeague, atomic = True)
        if str(reaction.emoji) == "💯":
            await member.add_roles(AllGames, atomic = True)
        if str(reaction.emoji) == "👊":
            await member.add_roles(FightingGames, atomic = True)

@client.event
async def on_reaction_remove(reaction, member):
    #removed server specific data#
    welcomeChannelID = CHANNEL_ID_GOES_HERE
    if reaction.message.channel.id == welcomeChannelID:
        BlackOps4 = discord.utils.get(member.guild.roles, name='BlackOps4')
        Fortnite = discord.utils.get(member.guild.roles, name='Fortnite')
        CSGO = discord.utils.get(member.guild.roles, name='CS:GO')
        League = discord.utils.get(member.guild.roles, name='LeagueOfLegends')
        DOTA = discord.utils.get(member.guild.roles, name='DOTA2')
        Overwatch = discord.utils.get(member.guild.roles, name='Overwatch')
        PUBG = discord.utils.get(member.guild.roles, name='PUBG')
        RocketLeague = discord.utils.get(member.guild.roles, name='RocketLeague')
        AllGames = discord.utils.get(member.guild.roles, name='AllGames')
        FightingGames = discord.utils.get(member.guild.roles, name='FightingGames') 
        if str(reaction.emoji) == "<:bo4:510614885336350742>":
            await member.remove_roles(BlackOps4, atomic = True)
        if str(reaction.emoji) == "<:fortnite:510614994283528193>":
            await member.remove_roles(Fortnite, atomic = True)
        if str(reaction.emoji) == "<:csgo:510615696162422794>":
            await member.remove_roles(CSGO, atomic = True)
        if str(reaction.emoji) == "<:league:510615023836725248>":
            await member.remove_roles(League, atomic = True)
        if str(reaction.emoji) == "<:dota:510614956358500352>":
            await member.remove_roles(DOTA, atomic = True)
        if str(reaction.emoji) == "<:overwatch:510615060276707348>":
            await member.remove_roles(Overwatch, atomic = True)
        if str(reaction.emoji) == "<:pubg:510615088655368193>":
            await member.remove_roles(PUBG, atomic = True)
        if str(reaction.emoji) == "<:rocketleague:510615116002230290>":
            await member.remove_roles(RocketLeague, atomic = True)
        if str(reaction.emoji) == "💯":
            await member.remove_roles(AllGames, atomic = True)
        if str(reaction.emoji) == "👊":
            await member.remove_roles(FightingGames, atomic = True)          
            
#check if a user is streaming, if they are assign them role of streaming for visibility purposes    
@client.event
async def on_member_update(before, after):

    channel = client.get_channel(CHENNEL_ID_GOES_HERE)
    Streams = discord.utils.get(after.guild.roles, name='Streams')
    if str(after.activity.type) != "ActivityType.streaming":
        return
    elif str(before.activity.type) == "ActivityType.streaming" and str(after.activity.type) == "ActivityType.streaming":
        return
    elif str(before.activity.type) != "ActivityType.streaming" and str(after.activity.type) == "ActivityType.streaming":
        await after.add_roles(Streams, atomic = True)
    else:
        await after.remove_roles(Streams, atomic = True) 

#loop the streams checker, boot the ol' bot up
client.run(TOKEN)

























