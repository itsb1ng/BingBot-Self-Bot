import discord
from discord.ext import commands
import requests
import os
import shutil
from playsound import playsound
import time
import json
import asyncio
from discord import Webhook, RequestsWebhookAdapter, Embed
import datetime
import subprocess
import math
import sys

""""
MAKING AN ATTEMPT TO ADD OR REMOVE FROM THE CODE MAY RESULT IN THE BREAKING OF THE SCRIPT. IF YOU HAVE ANY FURTHER QUESTIONS
PLEASE CONTACT ME VIA DISCORD: https://discord.gg/Nh6wgyfAPR. 

GITHUB REPOSITORY: https://github.com/itsb1ng/BingBot-Self-Bot
"""

with open("config.json", "r") as f:
    config = json.load(f)

DISCORD_TOKEN = config['discord_token']
PREFIX = config['prefix']
DM_WEBHOOK = config['webhook']
API_KEY = config['api_key']
STATUS = config['discord_status']

global width
width = os.get_terminal_size().columns
def startup(setting):
    print()
    print()
    if setting == "standard" or setting == "":
        print("██████╗ ██╗███╗   ██╗ ██████╗ ██████╗  ██████╗ ████████╗".center(width))
        print("██╔══██╗██║████╗  ██║██╔════╝ ██╔══██╗██╔═══██╗╚══██╔══╝".center(width))
        print("██████╔╝██║██╔██╗ ██║██║  ███╗██████╔╝██║   ██║   ██║   ".center(width))
        print("██╔══██╗██║██║╚██╗██║██║   ██║██╔══██╗██║   ██║   ██║   ".center(width))
        print("██████╔╝██║██║ ╚████║╚██████╔╝██████╔╝╚██████╔╝   ██║   ".center(width))
        print("╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   ".center(width))
    elif setting == "3D":
        print(r"________  ___  ________   ________  ________  ________  _________    ".center(width))
        print(r"|\   __  \|\  \|\   ___  \|\   ____\|\   __  \|\   __  \|\___   ___\ ".center(width))
        print(r"\ \  \|\ /\ \  \ \  \\ \  \ \  \___|\ \  \|\ /\ \  \|\  \|___ \  \_| ".center(width))
        print(r" \ \   __  \ \  \ \  \\ \  \ \  \  __\ \   __  \ \  \\\  \   \ \  \  ".center(width))
        print(r"  \ \  \|\  \ \  \ \  \\ \  \ \  \|\  \ \  \|\  \ \  \\\  \   \ \  \ ".center(width))
        print(r"   \ \_______\ \__\ \__\\ \__\ \_______\ \_______\ \_______\   \ \__\ ".center(width))
        print(r"    \|_______|\|__|\|__| \|__|\|_______|\|_______|\|_______|    \|__|".center(width))
    elif setting == "pointed":
        print(r"▀█████████▄   ▄█  ███▄▄▄▄      ▄██████▄  ▀█████████▄   ▄██████▄      ███     ".center(width))
        print(r"  ███    ███ ███  ███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ▀█████████▄ ".center(width))
        print(r"  ███    ███ ███▌ ███   ███   ███    █▀    ███    ███ ███    ███    ▀███▀▀██ ".center(width))
        print(r" ▄███▄▄▄██▀  ███▌ ███   ███  ▄███         ▄███▄▄▄██▀  ███    ███     ███   ▀ ".center(width))
        print(r"▀▀███▀▀▀██▄  ███▌ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀██▄  ███    ███     ███     ".center(width))
        print(r"  ███    ██▄ ███  ███   ███   ███    ███   ███    ██▄ ███    ███     ███     ".center(width))
        print(r"  ███    ███ ███  ███   ███   ███    ███   ███    ███ ███    ███     ███     ".center(width))
        print(r"▄█████████▀  █▀    ▀█   █▀    ████████▀  ▄█████████▀   ▀██████▀     ▄████▀   ".center(width))
    elif setting == "money":
        print(r"$$$$$$$\  $$$$$$\ $$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$\ $$$$$$$$\ ".center(width))
        print(r"$$  __$$\ \_$$  _|$$$\  $$ |$$  __$$\ $$  __$$\ $$  __$$\\__$$  __|".center(width))
        print(r"$$ |  $$ |  $$ |  $$$$\ $$ |$$ /  \__|$$ |  $$ |$$ /  $$ |  $$ |   ".center(width))
        print(r"$$$$$$$\ |  $$ |  $$ $$\$$ |$$ |$$$$\ $$$$$$$\ |$$ |  $$ |  $$ |   ".center(width))
        print(r"$$  __$$\   $$ |  $$ \$$$$ |$$ |\_$$ |$$  __$$\ $$ |  $$ |  $$ |   ".center(width))
        print(r"$$ |  $$ |  $$ |  $$ |\$$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |   ".center(width))
        print(r"$$$$$$$  |$$$$$$\ $$ | \$$ |\$$$$$$  |$$$$$$$  | $$$$$$  |  $$ |   ".center(width))
        print(r"\_______/ \______|\__|  \__| \______/ \_______/  \______/   \__|   ".center(width))
    elif setting == "blocks":
        print(r" .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------. ".center(width))
        print(r"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |".center(width))
        print(r"| |   ______     | || |     _____    | || | ____  _____  | || |    ______    | || |   ______     | || |     ____     | || |  _________   | |".center(width))
        print(r"| |  |_   _ \    | || |    |_   _|   | || ||_   \|_   _| | || |  .' ___  |   | || |  |_   _ \    | || |   .'    `.   | || | |  _   _  |  | |".center(width))
        print(r"| |    | |_) |   | || |      | |     | || |  |   \ | |   | || | / .'   \_|   | || |    | |_) |   | || |  /  .--.  \  | || | |_/ | | \_|  | |".center(width))
        print(r"| |    |  __'.   | || |      | |     | || |  | |\ \| |   | || | | |    ____  | || |    |  __'.   | || |  | |    | |  | || |     | |      | |".center(width))
        print(r"| |   _| |__) |  | || |     _| |_    | || | _| |_\   |_  | || | \ `.___]  _| | || |   _| |__) |  | || |  \  `--'  /  | || |    _| |_     | |".center(width))
        print(r"| |  |_______/   | || |    |_____|   | || ||_____|\____| | || |  `._____.'   | || |  |_______/   | || |   `.____.'   | || |   |_____|    | |".center(width))
        print(r"| |              | || |              | || |              | || |              | || |              | || |              | || |              | |".center(width))
        print(r"| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |".center(width))
        print(r" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ".center(width))
    elif setting == "graffiti":
        print(r"__________.___ _______    __________________ ___________________".center(width))
        print(r"\______   \   |\      \  /  _____/\______   \\_____  \__    ___/".center(width))
        print(r" |    |  _/   |/   |   \/   \  ___ |    |  _/ /   |   \|    |   ".center(width))
        print(r" |    |   \   /    |    \    \_\  \|    |   \/    |    \    |   ".center(width))
        print(r" |______  /___\____|__  /\______  /|______  /\_______  /____|   ".center(width))
        print(r"        \/            \/        \/        \/         \/         ".center(width))
    elif setting == "slant":
        print(r" ______     __     __   __     ______     ______     ______     ______  ".center(width))
        print(r'/\  == \   /\ \   /\ "-.\ \   /\  ___\   /\  == \   /\  __ \   /\__  _\ '.center(width))
        print(r"\ \  __<   \ \ \  \ \ \-.  \  \ \ \__ \  \ \  __<   \ \ \/\ \  \/_/\ \/ ".center(width))
        print(r' \ \_____\  \ \_\  \ \_\\"\_\  \ \_____\  \ \_____\  \ \_____\    \ \_\ '.center(width))
        print(r"  \/_____/   \/_/   \/_/ \/_/   \/_____/   \/_____/   \/_____/     \/_/ ".center(width))
    else:
        print("██████  ██ ███    ██  ██████  ██████   ██████  ████████ ".center(width))
        print("██   ██ ██ ████   ██ ██       ██   ██ ██    ██    ██    ".center(width))
        print("██████  ██ ██ ██  ██ ██   ███ ██████  ██    ██    ██    ".center(width))
        print("██   ██ ██ ██  ██ ██ ██    ██ ██   ██ ██    ██    ██    ".center(width))
        print("██████  ██ ██   ████  ██████  ██████   ██████     ██    ".center(width))                                                        
    print("Created by bing#0001".center(width))                                            

def song(song):
    if song == "start":
        playsound(r"sounds\startup.mp3")
    elif song == "dm":
        playsound(r"sounds\dmsound.mp3")
    elif song == "failedlogin":
        playsound(r"sounds\failedlogin.mp3")

def getInfo(call):
    r = requests.get(call)
    return r.json()
        
bing = commands.Bot(command_prefix=PREFIX, self_bot=True)

@bing.event
async def on_connect():
    print(f"Logged in as: {bing.user}\n")
    song("start")
    if STATUS == "dnd":
        await bing.change_presence(status=discord.Status.dnd)
    elif STATUS == "idle":
        await bing.change_presence(status=discord.Status.idle)
    else:
        await bing.change_presence(status=discord.Status.online)

@bing.event
async def on_message(message):
    if message.author.id == bing.user.id:
        with open("commands.json", "r") as f:
            cmds = json.load(f)
        for command in cmds:
            if f"{PREFIX}{command}" in message.content:
                try:
                    await message.delete()
                    print("Command: " + message.content)
                    ctx = await bing.get_context(message)
                    await bing.invoke(ctx)
                except:
                    pass
    if (message.author.id != bing.user.id) and (message.channel.type is discord.ChannelType.private):
        if DM_WEBHOOK != "":
            try:
                webhook = Webhook.from_url(DM_WEBHOOK, adapter=RequestsWebhookAdapter())
                embed = discord.Embed(title="Received DM", color=0xC98FFC)
                embed.add_field(name="User:",value=message.author,inline=False)
                embed.add_field(name="User ID:",value=message.author.id,inline=False)
                if int(message.created_at.strftime("%H")) > 12:
                    hour = int(message.created_at.strftime("%H")) - 10
                else: 
                    hour = message.created_at.strftime("%H")
                embed.add_field(name="Received:",value=message.created_at.strftime(f"%A, %B %d %Y @ {hour}:%M %p GMT+2"),inline=False)
                embed.set_thumbnail(url="https://i.imgur.com/sKwqOXE.png")
                embed.set_footer(text="BingBot Self-Bot", icon_url="https://i.imgur.com/sKwqOXE.png")
                song("dm")
                print(f"Received Direct Message: {message.author}")
                webhook.send(embed=embed)
            except:
                pass

@bing.command()
async def pornhub(ctx, firstword, secondword):
    image = requests.get(f"https://logohub.appspot.com/{firstword}-{secondword}-120.webp?scheme=white&transparent=true&padding=0", stream=True)
    if image.status_code == 200:
        image.raw.decode_content = True
        with open("image.png",'wb') as f:
            shutil.copyfileobj(image.raw, f)
    file = discord.File("image.png", filename="image.png")
    await ctx.send(file=file)
    os.remove("image.png")

@bing.command()
async def servers(ctx):
    await ctx.send(f"{bing.user} is currently in {len(bing.guilds)} Discord Servers")

@bing.command()
async def friends(ctx):
    await ctx.send(f"{bing.user} currently has {len(bing.user.friends)} Users Friended")

@bing.command()
async def selfpurge(ctx, num):
    time.sleep(1)
    messagehistory = await ctx.channel.history(limit=int(num)).flatten()
    messagesdeleted = 0
    for message in messagehistory:
        if message.author.id == bing.user.id:
            try:
                messagesdeleted+=1
                await message.delete()
                await asyncio.sleep(2)
            except:
                pass
    await ctx.send(f"`You have deleted {messagesdeleted} messages`")

@bing.command()
async def hypixelstats(ctx, name):
    try:
        user_name = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
        uuid = user_name["id"]
        link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
        data = getInfo(link)

        rank = data['player']['newPackageRank']
        if "_" in rank:
            rank = rank.replace("_PLUS","+")
        if "MVP" in rank:
            if data['player']['monthlyPackageRank'] != "NONE":
                rank = rank + "+"
        
        level = ((math.sqrt(data['player']['networkExp'] + 15312.5) - (125/math.sqrt(2))) / 25 * math.sqrt(2)) / 2
        await ctx.send("```\n\t\t{}'s Hypixel Statistics:\nHypixel Rank: {}\nKarma: {:,}\nNetwork XP: {:,.2f}\nHypixel Level: {:.2f}\n```\nhttps://crafatar.com/renders/body/{}".format(name, rank, data['player']['karma'], data['player']['networkExp'], level, uuid))
    except:
        await ctx.send("```\nError:\nInvalid IGN\n```")

@bing.command()
async def skills(ctx, name):
    if API_KEY != "":
        try:
            user_name = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
            uuid = user_name["id"]
            profile_link = f"https://api.hypixel.net/skyblock/profiles?key={API_KEY}&uuid={uuid}"
            sb_data = getInfo(profile_link)
            link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
            data = getInfo(link)
            senither = f"https://hypixel-api.senither.com/v1/profiles/{uuid}?key={API_KEY}"
            senither_data = getInfo(senither)
            save = 9999999999999999999
            for x in range(0, len(sb_data['profiles'])):
                for y in sb_data['profiles'][x]['members']:
                    if uuid == y:
                        difference = time.time() - sb_data['profiles'][x]['members'][y]['last_save']
                        if difference < save:
                            save = sb_data['profiles'][x]['members'][y]['last_save']
                            profile_id = sb_data['profiles'][x]['profile_id']

            for z in range(0,len(senither_data['data'])):
                if senither_data['data'][z]['id'] == profile_id:
                    profile_num = z

            profile_name = data['player']['stats']['SkyBlock']['profiles'][profile_id]["cute_name"]

            def farming():
                try:
                    senither_data['data'][profile_num]['skills']['farming']['level']
                    return senither_data['data'][profile_num]['skills']['farming']['level']
                except:
                    return 0

            def mining():
                try:
                    senither_data['data'][profile_num]['skills']['mining']['level']
                    return senither_data['data'][profile_num]['skills']['mining']['level']
                except:
                    return 0

            def combat():
                try:
                    senither_data['data'][profile_num]['skills']['combat']['level']
                    return senither_data['data'][profile_num]['skills']['combat']['level']
                except:
                    return 0

            def foraging():
                try:
                    senither_data['data'][profile_num]['skills']['foraging']['level']
                    return senither_data['data'][profile_num]['skills']['foraging']['level']
                except:
                    return 0

            def fishing():
                try:
                    senither_data['data'][profile_num]['skills']['fishing']['level']
                    return senither_data['data'][profile_num]['skills']['fishing']['level']
                except:
                    return 0

            def enchanting():
                try:
                    senither_data['data'][profile_num]['skills']['enchanting']['level']
                    return senither_data['data'][profile_num]['skills']['enchanting']['level']
                except:
                    return 0

            def alchemy():
                try:
                    senither_data['data'][profile_num]['skills']['alchemy']['level']
                    return senither_data['data'][profile_num]['skills']['alchemy']['level']
                except:
                    return 0

            def taming():
                try:
                    senither_data['data'][profile_num]['skills']['taming']['level']
                    return senither_data['data'][profile_num]['skills']['taming']['level']
                except:
                    return 0

            def skill_average():
                try:
                    senither_data['data'][profile_num]['skills']['average_skills']
                    return senither_data['data'][profile_num]['skills']['average_skills']
                except:
                    return 0
            
            await ctx.send("```\n\t\t{}'s Skyblock Skills:\nActive Profile: {}\nSkill Average: {:,.1f}\nFarming: {:.0f}\nMining: {:.0f}\nCombat: {:.0f}\nForaging: {:.0f}\nFishing: {:.0f}\nEnchanting: {:.0f}\nAlchemy: {:.0f}\nTaming: {:.0f}\n```".format(name,profile_name,skill_average(),farming(),mining(),combat(),foraging(),fishing(),enchanting(),alchemy(),taming()))
        except:
            await ctx.send("```\nError:\nInvalid IGN\n```")
    else:
        await ctx.send("`Invalid API Key`")

@bing.command()
async def weight(ctx, name):
    if API_KEY != "":
        try:
            user_name = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
            uuid = user_name["id"]
            profile_link = f"https://api.hypixel.net/skyblock/profiles?key={API_KEY}&uuid={uuid}"
            sb_data = getInfo(profile_link)
            link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
            data = getInfo(link)
            senither = f"https://hypixel-api.senither.com/v1/profiles/{uuid}?key={API_KEY}"
            senither_data = getInfo(senither)
            save = 9999999999999999999
            for x in range(0, len(sb_data['profiles'])):
                for y in sb_data['profiles'][x]['members']:
                    if uuid == y:
                        difference = time.time() - sb_data['profiles'][x]['members'][y]['last_save']
                        if difference < save:
                            save = sb_data['profiles'][x]['members'][y]['last_save']
                            profile_id = sb_data['profiles'][x]['profile_id']

            for z in range(0,len(senither_data['data'])):
                if senither_data['data'][z]['id'] == profile_id:
                    profile_num = z

            profile_name = data['player']['stats']['SkyBlock']['profiles'][profile_id]["cute_name"]

            def weight():
                try:
                    senither_data['data'][profile_num]['weight']
                    return senither_data['data'][profile_num]['weight']
                except:
                    return 0

            def overflow():
                try:
                    senither_data['data'][profile_num]['weight_overflow']
                    return senither_data['data'][profile_num]['weight_overflow']
                except:
                    return 0

            def total_weight():
                return overflow() + weight()

            await ctx.send("```\n\t\t{}'s Skyblock Weight:\nActive Profile: {}\nWeight: {:,.2f}\nOverflow Weight: {:,.2f}\nTotal Weight: {:,.2f}\n```".format(name,profile_name,weight(),overflow(),total_weight()))
        except:
            await ctx.send("```\nError:\nInvalid IGN\n```")
    else:
        await ctx.send("`Invalid API Key`")

@bing.command()
async def slayer(ctx, name):
    if API_KEY != "":
        try:
            user_name = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
            uuid = user_name["id"]
            profile_link = f"https://api.hypixel.net/skyblock/profiles?key={API_KEY}&uuid={uuid}"
            sb_data = getInfo(profile_link)
            link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
            data = getInfo(link)
            save = 9999999999999999999
            for x in range(0, len(sb_data['profiles'])):
                for y in sb_data['profiles'][x]['members']:
                    if uuid == y:
                        difference = time.time() - sb_data['profiles'][x]['members'][y]['last_save']
                        if difference < save:
                            save = sb_data['profiles'][x]['members'][y]['last_save']
                            profile_id = sb_data['profiles'][x]['profile_id']

            for z in range(0,len(sb_data['profiles'])):
                if sb_data['profiles'][z]['profile_id'] == profile_id:
                    profile_num = z

            profile_name = data['player']['stats']['SkyBlock']['profiles'][profile_id]["cute_name"]

            SPIDER_XP = sb_data['profiles'][profile_num]['members'][uuid]['slayer_bosses']['spider']['xp']
            if int(SPIDER_XP) > 1000000:
                SPIDER_LVL = "9"
            elif int(SPIDER_XP) > 400000:
                SPIDER_LVL = "8"
            elif int(SPIDER_XP) > 100000:
                SPIDER_LVL = "7"
            elif int(SPIDER_XP) > 20000:
                SPIDER_LVL = "6"
            elif int(SPIDER_XP) > 5000:
                SPIDER_LVL = "5"
            elif int(SPIDER_XP) > 1000:
                SPIDER_LVL = "4"
            elif int(SPIDER_XP) > 200:
                SPIDER_LVL = "3"
            elif int(SPIDER_XP) > 25:
                SPIDER_LVL = "2"
            elif int(SPIDER_XP) > 5:
                SPIDER_LVL = "1"
            else:
                SPIDER_LVL = "0"

            REV_XP = sb_data['profiles'][profile_num]['members'][uuid]['slayer_bosses']['zombie']['xp']
            if int(REV_XP) > 1000000:
                REV_LVL = "9"
            elif int(REV_XP) > 400000:
                REV_LVL = "8"
            elif int(REV_XP) > 100000:
                REV_LVL = "7"
            elif int(REV_XP) > 20000:
                REV_LVL = "6"
            elif int(REV_XP) > 5000:
                REV_LVL = "5"
            elif int(REV_XP) > 1000:
                REV_LVL = "4"
            elif int(REV_XP) > 200:
                REV_LVL = "3"
            elif int(REV_XP) > 15:
                REV_LVL = "2"
            elif int(REV_XP) > 5:
                REV_LVL = "1"
            else:
                REV_LVL = "0"

            SVEN_XP = sb_data['profiles'][profile_num]['members'][uuid]['slayer_bosses']['wolf']['xp']
            if int(SVEN_XP) > 1000000:
                SVEN_LVL = "9"
            elif int(SVEN_XP) > 400000:
                SVEN_LVL = "8"
            elif int(SVEN_XP) > 100000:
                SVEN_LVL = "7"
            elif int(SVEN_XP) > 20000:
                SVEN_LVL = "6"
            elif int(SVEN_XP) > 5000:
                SVEN_LVL = "5"
            elif int(SVEN_XP) > 1500:
                SVEN_LVL = "4"
            elif int(SVEN_XP) > 250:
                SVEN_LVL = "3"
            elif int(SVEN_XP) > 30:
                SVEN_LVL = "2"
            elif int(SVEN_XP) > 10:
                SVEN_LVL = "1"
            else:
                SVEN_LVL = "0"

            ENDER_XP = sb_data['profiles'][profile_num]['members'][uuid]['slayer_bosses']['enderman']['xp']
            if int(ENDER_XP) > 1000000:
                ENDER_LVL = "9"
            elif int(ENDER_XP) > 400000:
                ENDER_LVL = "8"
            elif int(ENDER_XP) > 100000:
                ENDER_LVL = "7"
            elif int(ENDER_XP) > 20000:
                ENDER_LVL = "6"
            elif int(ENDER_XP) > 5000:
                ENDER_LVL = "5"
            elif int(ENDER_XP) > 1500:
                ENDER_LVL = "4"
            elif int(ENDER_XP) > 250:
                ENDER_LVL = "3"
            elif int(ENDER_XP) > 30:
                ENDER_LVL = "2"
            elif int(ENDER_XP) > 10:
                ENDER_LVL = "1"
            else:
                ENDER_LVL = "0"

            await ctx.send("```\n\t\t{}'s Slayer XP and Levels\nActive profile: {}\n\nRevenant Horror: Level {}\nSlayer XP {:,.0f}\n\nTarantula Broodfather: Level {}\nSlayer XP {:,.0f}\n\nSven Packmaster: Level {}\nSlayer XP {:,.0f}\n\nVoidgloom Seraph: Level {}\nSlayer XP {:,.0f}\n```".format(name, profile_name, REV_LVL, REV_XP, SPIDER_LVL, SPIDER_XP, SVEN_LVL, SVEN_XP, ENDER_LVL, ENDER_XP))
        except:
            await ctx.send("```\nError:\nInvalid IGN\n```")
    else:
        await ctx.send("`Invalid API Key`")

startup(config['startup'])
try:
    bing.run(DISCORD_TOKEN)
except:
    song("failedlogin")
    exit("Invalid Discord Token\n")