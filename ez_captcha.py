#!/usr/bin/python3


############                    >>>>            E D I T    B E L O W !!!            <<<<
class settings:
    
    
    #Required > 
    ############################################################################################################
    verified_role_given = 000000000000000000 # < <  < Role ID here <--                                                                                         <-----------|REQUIRED|
    verification_channel = 000000000000000000# < <  < Channel ID here <--                                                                                  <----------|REQUIRED|
    welcome_channel = 000000000000000000 # < <  < Channel ID here <--                                                                                      <----------|REQUIRED|
    Token = "NjI1NTM2MjkyNjMzMDUxMTM3.XYlTpA.wxfXKM6uKiPLffskYkS_" # Your token goes here <<     <----------|REQUIRED|
    ############################################################################################################
    
    #Aesthetics >
    ############################################################################################################
    prefix = "&&" # < < SET YOUR COMMAND PREFIX <--
    rich_presence = f"{prefix}help || https://host-info.net" #(Activity Context: "Watching [" "]")
    captcha_image_big = "https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png"
    welcome_emote_1 = "" #< Paste Emote
    welcome_emote_2 = "" #< Paste Emote
    mag_glass_user_emote = ""#< Paste Emote
    ############################################################################################################
    
    #Logging >
    ############################################################################################################
    error_log_channel = 000000000000000000 #Option to send errors/important stuff to a channel. < Channel ID here <--
    error_log_channel_enabled = 0 # CHANGE TO 1 TO ENABLE LOGGING TO A DISCORD CHANNEL WITHIN YOUR GUILD!
    ############################################################################################################

    #Binary >
    ############################################################################################################
    #Use "build_executable.py" to build binary.
    #Executable @ runtime, may speed up operations.
    #I will add cython support as well 
    #Use `get_color_hex()` in-place of the hex colors in the embeds for random colors
    ############################################################################################################

    



##############################################################################################################
from time import sleep
from os import system
from sys import argv
from subprocess import PIPE, run
from random import choice



try: 
    import discord
except Exception as E:
    installed = False
    print(str(E))
    try:
        stack = ['pip3', 'install', 'discord']
        run(stack)
        installed = True
    except Exception as EE:
        installed = False
        print(str(EE))
        try:
            print("Trying ALT PATH...");sleep(5)
            stack[0] = str(stack[0].replace("3",""))
            run(stack)
            installed = True
        except Exception as e:
            print(str(e))
            sleep(5)
    if installed == True:
        print('\nSuccessfully Installed Discord Official API!')
        sleep(1)
    else:
        print('\nCould Not PIP Install Discord Official API!!!\nMaybe This Will Help ;) \n\nhttps://appuals.com/fix-pip-is-not-recognized-as-an-internal-or-external-command/#targetText='
              'Then%2C%20type%20%E2%80%9Ccmd%E2%80%9D%20and,present%20in%20the%20PATH%20variable\nOr Try Manually Installing "discord" Module / "pyinstaller"\n\nExiting...')
        sleep(5)
        exit(0)



    
       
import requests, sys, random, platform
from os import remove, getcwd
from io import StringIO
from random import randint, choice


print("\nStarting Service - Standby For Login Message!", end="")

    
class strings:
    help_text=f"""
```yaml
[Bot Commands]
--------------------------------------------------------------------------
Help:
'{settings.prefix}help' - Get Commands List

Information:
'{settings.prefix}user.info @USER' - Gets Some Info On A Member.
'{settings.prefix}system' - Gets System Info.
--------------------------------------------------------------------------
```
"""

last_user_accepted = ""
first_captcha = True
current_captcha = " " 
count = 0
bot_count = 0    
not_null = " "
null = ""
client=discord.Client()

@client.event
async def on_ready():
    print('-\n[Ok] - Succesfully logged in as {0.user} Via Discord Official API!'.format(client))
    activity = discord.Activity(name=settings.rich_presence, type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print(f'Displaying RP: ["Watching {settings.rich_presence}"]')
   
    
@client.event
async def on_message(message):
    if message.author == client.user:
        #await message.add_reaction(settings.mag_glass_user_emote) #spammy
        return

    global count, bot_count
    count += 1
    if message.author.bot == True:
        bot_count += 1 
        #await message.add_reaction('BOT_EMOJI_HERE') #spammy
        
            
            
            
    if message.channel.id == settings.verification_channel:
        await message.delete()
        global current_captcha
        first = False
        if len(current_captcha) < 6:
            first = True
            current_captcha = const()
            await message.channel.purge(limit=100, check=None, before=None, after=None, around=None, oldest_first=False, bulk=True)
            embed = embed_captcha(message.author, current_captcha, message.guild.name, message.guild.icon)
            await message.channel.send(not_null, embed=embed)        
        else:        
            if message.content == current_captcha:
                er = False
                try:
                    role = discord.utils.get(message.guild.roles, id=settings.verified_role_given)
                except Exception:
                    er = True
                if er == False:
                    try:
                        await message.author.add_roles(role)    
                    except Exception:
                        er = True 
                    if er != False:
                        return    
                    else:
                        creation_date = discord.utils.snowflake_time(message.author.id)
                        member = discord.utils.get(message.guild.members, id=int(message.author.id))
                        avatar = str(member.avatar_url)
                        try:
                            current_act = str(member.activities)
                        except Exception:
                            current_act = "N/A"       
                        try:    
                            embed = discord.Embed(title=f"{settings.welcome_emote_1}A New User Has Been Verified!{settings.welcome_emote_1}\n{settings.welcome_emote_2}Welcome To {message.guild.name}!{settings.welcome_emote_2}", description=" ", url='http://aero-bot.pro/', color=0x860111)
                            embed.set_author(name=f"{message.author}", url=' ', icon_url=avatar)
                            if message.guild.icon is not None:
                                #embed.set_thumbnail(url=message.guild.icon)    #todo > Returns Malformed URL Body
                                embed.set_thumbnail(url=settings.captcha_image_big)
                            else:
                                embed.set_thumbnail(url=settings.captcha_image_big)
                            embed.add_field(name="__User:__", value=str(message.author), inline=False)
                            embed.add_field(name="__ID:__", value=f"{str(message.author.id)}", inline=False)
                            embed.add_field(name="__Creation - Date/Time:__", value=creation_date, inline=False)
                            embed.add_field(name="__Joined Server - Date/Time:__", value=message.author.joined_at)
                            embed.add_field(name="__Current Activity:__", value=current_act, inline=False)
                            embed.set_footer(text=f"Responding To Verification Event in #{message.channel}.")
                            channel = client.get_channel(settings.welcome_channel)
                            await channel.send(not_null, embed=embed)                        
                        except Exception as erro:
                            if settings.error_log_channel_enabled != 0:
                                log1 = client.get_channel(settings.error_log_channel)
                                await log1.send(f"ERROR FAILED TO SEND CONFIRMATION FOR {message.author}:\n{str(erro)}")                              

                elif er != False:
                    if settings.error_log_channel_enabled != 0:
                        log = client.get_channel(settings.error_log_channel)
                        await log.send(f"FAILED TO ASSIGN [{message.author}] WITH ROLE: [{settings.verified_role_given}]!")    

                if first == False:
                    current_captcha = const()
                    await message.channel.purge(limit=100, check=None, before=None, after=None, around=None, oldest_first=False, bulk=True)
                    embed = embed_captcha(message.author, current_captcha, message.guild.name, message.guild.icon)
                    await message.channel.send(" ", embed=embed)
                
                
                
#### IP LOGGER DETECTION ###################################

                
#Possible Loggers
                
    if message.content.startswith(".co") or message.content.startswith("grabify.link") or message.content.startswith("ip"):
        await message.delete()
        await message.channel.send(f"**{message.author} MAY have just attempted to drop an IP Logger in channel {message.channel.name}!\nRAW PROOF:\n```css\n{message.content}\n```**")
        await message.channel.send(f"@ADMIN  ^^^")

#Definitley Loggers        

    if message.content.startswith("https://iplogger.org/") or message.content.startswith("https://2no.co/") or message.content.startswith("https://ez.stat/"):
        await message.delete()
        await message.channel.send(f"**{message.author} MAY have just attempted to drop an IP Logger in channel {message.channel.name}!\nRAW PROOF:\n```css\n{message.content}\n```\n**Message ID: {message.id}**")
        await message.channel.send(f"@ADMIN  ^^^")
        
    if message.content.startswith("https://02ip.ru/") or message.content.startswith("https://iplo.ru/") or message.content.startswith("https://iplis.ru/") or message.content.startswith("https://yip.su/"):
        await message.delete()
        await message.channel.send(f"**{message.author} MAY have just attempted to drop an IP Logger in channel {message.channel.name}!\nRAW PROOF:\n```css\n{message.content}\n```\n**Message ID: {message.id}**")
        await message.channel.send(f"@ADMIN  ^^^")
        
    if message.content.startswith("https://02ip.ru/") or message.content.startswith("https://ipgrabber.ru/") or message.content.startswith("https://iplogger.info/") or message.content.startswith("https://ipgraber.ru/"):
        await message.delete()
        await message.channel.send(f"**{message.author} MAY have just attempted to drop an IP Logger in channel {message.channel.name}!\nRAW PROOF:\n```css\n{message.content}\n```\n**Message ID: {message.id}**")
        await message.channel.send(f"@ADMIN  ^^^")         
        
    if message.content.startswith("https://") or message.content.startswith("http://"):
        await message.channel.send(f":eyes: **__{message.author} Posted A Link!__** :eyes:")
#################################################################        
        
    if message.content.startswith(f"{settings.prefix}uptime") or message.content.startswith(f"{settings.prefix}system"):
        try:
            uptime = subprocess.check_output("uptime")
            uptime = uptime.decode("utf-8")
        except Exception:
            uptime = "I'm in a testing environment right now, check back later :)"
        up = uptime.replace(",", " |")
        embed = discord.Embed(title=f"Gatekeeper System Info", description=" ", url='http://aero-bot.pro/', color=0x860111)
        embed.set_author(name="Gatekeeper", url='http://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/610035652112810024/620167625774727178/1_h4YRd-tMvBGSVhAXtzYbKA_1.png")
        embed.add_field(name="__Current Uptime:__", value=up, inline=False)
        embed.add_field(name="__Requests Since Boot:__", value=str(count), inline=False)
        embed.add_field(name="__System:__", value=str(platform.system()), inline=False)
        embed.add_field(name="__Node:__", value=str(str(platform.node().replace("0", "x").replace("1", "x").replace("2", "x").replace("3", "x").replace("4", "x").replace("5", "x").replace("6", "x").replace("7", "x").replace("8", "x").replace("9", "x"))), inline=False)
        embed.add_field(name="__Release:__", value=str(platform.release()), inline=False)
        embed.add_field(name="__Version:__", value=str(platform.version()), inline=False)
        embed.add_field(name="__Machine:__", value=str(platform.machine()), inline=False)
        embed.add_field(name="__Proccessor:__", value=str(platform.processor()), inline=False)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        await message.channel.send("**__System Info__**", embed=embed)
                           
    if message.content.startswith(f'{settings.prefix}user.info'):
        p1 = message.content.replace(f"{settings.prefix}","")
        p1 = p1.replace(" ", "").replace("<", "").replace("@", "").replace(">", "").replace("!", "")
        p1 = p1.replace("user.info", "")
        exx = False
        try:
            p1 = int(p1)
        except Exception:
            exx = True
            pass
        if exx == False:
            member = discord.utils.get(message.guild.members, id=p1)
            if member is not None and member.bot != True:
                name = str(member.display_name)
                start_date = str(discord.utils.snowflake_time(member.id))
                block_char = str(bool(member.is_blocked()))
                avatar = str(member.avatar_url)
                mutual_guild = str(member.guild.name)
                join_date = str(member.joined_at)
                try:
                    current_act = str(member.activities)
                except Exception:
                    current_act = str("N/A")
                role = str(member.roles);role = role.replace("@", "")
                color = int(choice(colors.colors))
                embed = discord.Embed(title=f"User Info For\n", description=" ", url='http://aero-bot.pro/', color=color)
                embed.set_author(name="By Aero-Bot", url='http://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
                member = discord.utils.get(message.guild.members, id=int(message.author.id))             
                embed.set_thumbnail(url=member.avatar_url)
                embed.add_field(name="__User:__", value=name, inline=False)
                embed.add_field(name="__Nickname:__", value=str(member.nick), inline=False)
                embed.add_field(name="__ID:__", value=f"{str(p1)}", inline=False)
                embed.add_field(name="__Creation Date:__", value=start_date, inline=False)
                embed.add_field(name="__Mutual Server:__", value=mutual_guild, inline=False)
                embed.add_field(name="__Server Owner:__", value=str(message.guild.owner), inline=False)
                embed.add_field(name="__Server Region:__", value=str(message.guild.region), inline=False)
                embed.add_field(name="__Joined Server:__", value=join_date, inline=False)
                embed.add_field(name="__Current Status:__", value=f"{member.status}", inline=False)
                embed.add_field(name="__Blocked Bot:__", value=str(block_char+"\n---------------------------\n"), inline=False)
                embed.add_field(name="__Current Activity:__", value=current_act, inline=False)
                embed.add_field(name="__Current Roles:__", value=str(role), inline=False)
                embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
                await message.channel.send("**__User Info__**", embed=embed)
        else:
            await message.channel.send(f"Member [{p1}] Not Found In Guild(Or Not Accessible)!")

    if message.content.startswith(f'{settings.prefix}help') or message.content.startswith('$help') or message.content.startswith('!help') or message.content.startswith('&help'):
        await message.channel.send(f"\n**Hello, {message.author}.\n{strings.help_text}**")

class colors:
    colors = [
    0x860111,
    0x00FF00,
    0x041C4B,
    0xB723A5,
    0xECBF1B,
    0xF05C15
              ]
    def get_color_hex():
        return choice(colors)
    
class chars:
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v', 
    'w','x','y','z','1','2','3','4','5','6','7','8','9','!','$','%','^','*','(',')','-','_','=','+','/',
    ',','.',':',"'",'"','<','>','&','?']
    
def const():
    captcha = str(choice(chars.chars)+choice(chars.chars)+choice(chars.chars)+choice(chars.chars)+choice(chars.chars)+choice(chars.chars))
    return captcha

def embed_captcha(author, current_captcha, server, server_icon):
    embed = discord.Embed(title=f"Captcha Challenge\n", description=" ", url='http://aero-bot.pro/', color=0x860111)
    if server_icon is not None:
        #embed.set_thumbnail(url=message.guild.icon)    #todo > Returns Malformed URL Body
        embed.set_thumbnail(url=settings.captcha_image_big)
    else:
        embed.set_thumbnail(url=settings.captcha_image_big)
    embed.set_author(name=server, url='http://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
    embed.add_field(name="__How To Enter:__", value="Enter the Captcha below.", inline=False)
    embed.add_field(name="__Captcha:__", value=f"||{current_captcha}||", inline=False)
    embed.set_footer(text=f"Last User Verified: {author}.")
    return embed  
    
############################################    
client.run(settings.Token)
