import discord
from discord.ext import commands
import discord_self_embed
import requests
import os
import shutil
from playsound import playsound
import time
import json
import asyncio
from discord import Webhook, RequestsWebhookAdapter, Embed
from datetime import datetime
import subprocess
import math
import sys
from dotenv import load_dotenv
import pytz
from pytz import timezone

""""
MAKING AN ATTEMPT TO ADD OR REMOVE FROM THE CODE MAY RESULT IN THE BREAKING OF THE SCRIPT. IF YOU HAVE ANY FURTHER QUESTIONS
PLEASE CONTACT ME VIA DISCORD: https://discord.gg/Nh6wgyfAPR. 

GITHUB REPOSITORY: https://github.com/itsb1ng/BingBot-Self-Bot
"""

load_dotenv()

with open("config.json", "r") as f:
    config = json.load(f)

DISCORD_TOKEN = config[0]['discord_token']
PREFIX = config[0]['prefix']
DM_WEBHOOK = config[0]['dm_webhook']
API_KEY = config[0]['api_key']
STATUS = config[0]['discord_status']
NITRO_WEBHOOK = config[0]["nitro_webhook"]
EMBED_MODE = config[0]['embed_mode']

if PREFIX == "":
    PREFIX == "b!"

bing = commands.Bot(command_prefix=PREFIX, self_bot=True)

try:
    global width
    width = os.get_terminal_size().columns
    def startup(setting):
        print()
        print()
        if setting.lower() == "standard" or setting == "":
            print("██████╗ ██╗███╗   ██╗ ██████╗ ██████╗  ██████╗ ████████╗".center(width))
            print("██╔══██╗██║████╗  ██║██╔════╝ ██╔══██╗██╔═══██╗╚══██╔══╝".center(width))
            print("██████╔╝██║██╔██╗ ██║██║  ███╗██████╔╝██║   ██║   ██║   ".center(width))
            print("██╔══██╗██║██║╚██╗██║██║   ██║██╔══██╗██║   ██║   ██║   ".center(width))
            print("██████╔╝██║██║ ╚████║╚██████╔╝██████╔╝╚██████╔╝   ██║   ".center(width))
            print("╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   ".center(width))
        elif setting.lower() == "3d":
            print(r"________  ___  ________   ________  ________  ________  _________    ".center(width))
            print(r"|\   __  \|\  \|\   ___  \|\   ____\|\   __  \|\   __  \|\___   ___\ ".center(width))
            print(r"\ \  \|\ /\ \  \ \  \\ \  \ \  \___|\ \  \|\ /\ \  \|\  \|___ \  \_| ".center(width))
            print(r" \ \   __  \ \  \ \  \\ \  \ \  \  __\ \   __  \ \  \\\  \   \ \  \  ".center(width))
            print(r"  \ \  \|\  \ \  \ \  \\ \  \ \  \|\  \ \  \|\  \ \  \\\  \   \ \  \ ".center(width))
            print(r"   \ \_______\ \__\ \__\\ \__\ \_______\ \_______\ \_______\   \ \__\ ".center(width))
            print(r"    \|_______|\|__|\|__| \|__|\|_______|\|_______|\|_______|    \|__|".center(width))
        elif setting.lower() == "pointed":
            print(r"▀█████████▄   ▄█  ███▄▄▄▄      ▄██████▄  ▀█████████▄   ▄██████▄      ███     ".center(width))
            print(r"  ███    ███ ███  ███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ▀█████████▄ ".center(width))
            print(r"  ███    ███ ███▌ ███   ███   ███    █▀    ███    ███ ███    ███    ▀███▀▀██ ".center(width))
            print(r" ▄███▄▄▄██▀  ███▌ ███   ███  ▄███         ▄███▄▄▄██▀  ███    ███     ███   ▀ ".center(width))
            print(r"▀▀███▀▀▀██▄  ███▌ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀██▄  ███    ███     ███     ".center(width))
            print(r"  ███    ██▄ ███  ███   ███   ███    ███   ███    ██▄ ███    ███     ███     ".center(width))
            print(r"  ███    ███ ███  ███   ███   ███    ███   ███    ███ ███    ███     ███     ".center(width))
            print(r"▄█████████▀  █▀    ▀█   █▀    ████████▀  ▄█████████▀   ▀██████▀     ▄████▀   ".center(width))
        elif setting.lower() == "money":
            print(r"$$$$$$$\  $$$$$$\ $$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$\ $$$$$$$$\ ".center(width))
            print(r"$$  __$$\ \_$$  _|$$$\  $$ |$$  __$$\ $$  __$$\ $$  __$$\\__$$  __|".center(width))
            print(r"$$ |  $$ |  $$ |  $$$$\ $$ |$$ /  \__|$$ |  $$ |$$ /  $$ |  $$ |   ".center(width))
            print(r"$$$$$$$\ |  $$ |  $$ $$\$$ |$$ |$$$$\ $$$$$$$\ |$$ |  $$ |  $$ |   ".center(width))
            print(r"$$  __$$\   $$ |  $$ \$$$$ |$$ |\_$$ |$$  __$$\ $$ |  $$ |  $$ |   ".center(width))
            print(r"$$ |  $$ |  $$ |  $$ |\$$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |   ".center(width))
            print(r"$$$$$$$  |$$$$$$\ $$ | \$$ |\$$$$$$  |$$$$$$$  | $$$$$$  |  $$ |   ".center(width))
            print(r"\_______/ \______|\__|  \__| \______/ \_______/  \______/   \__|   ".center(width))
        elif setting.lower() == "blocks":
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
        elif setting.lower() == "graffiti":
            print(r"__________.___ _______    __________________ ___________________".center(width))
            print(r"\______   \   |\      \  /  _____/\______   \\_____  \__    ___/".center(width))
            print(r" |    |  _/   |/   |   \/   \  ___ |    |  _/ /   |   \|    |   ".center(width))
            print(r" |    |   \   /    |    \    \_\  \|    |   \/    |    \    |   ".center(width))
            print(r" |______  /___\____|__  /\______  /|______  /\_______  /____|   ".center(width))
            print(r"        \/            \/        \/        \/         \/         ".center(width))
        elif setting.lower() == "slant":
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
        elif song == ("nitro"):
            playsound(r"sounds\nitronotification.mp3")

    def getInfo(call):
        r = requests.get(call)
        return r.json()

    def bing_restart():
        python = sys.executable
        os.execl(python, python, * sys.argv)

    @bing.event
    async def on_connect():
        print(f"Logged in as: {bing.user}\n")
        song("start")
        if STATUS.lower() == "dnd":
            await bing.change_presence(status=discord.Status.dnd)
        elif STATUS.lower() == "idle":
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
        if (message.author.id != bing.user.id) and ("https://discord.gift/" in message.content):
            if (config[1]['nitro'] == "on"):
                try:
                    content = message.content.split(" ")
                    for item in content:
                        if "https://discord.gift/" in item:
                            GIFT_LINK = item
                    song("nitro")
                    print(f"\nNitro Sniped: {message.author}\n")
                    if NITRO_WEBHOOK != "":
                        try:
                            webhook = Webhook.from_url(NITRO_WEBHOOK, adapter=RequestsWebhookAdapter())
                            embed = discord.Embed(title="Nitro Gift", color=0xC98FFC)
                            embed.add_field(name="User:",value=message.author,inline=False)
                            embed.add_field(name="Link:",value=GIFT_LINK,inline=False)
                            MSG_LINK = message.jump_url
                            embed.add_field(name="Go To Message:",value=f"[Message Link]({MSG_LINK})",inline=False)
                            embed.set_thumbnail(url="https://static.roundme.com/upload/user/d30750eda6c30bba9295ad629961420555c05496.png")
                            embed.set_footer(text="BingBot Self-Bot", icon_url="https://i.imgur.com/sKwqOXE.png")
                            webhook.send(embed=embed)
                        except:
                            pass
                except:
                    pass
        if (message.author.id != bing.user.id) and (message.channel.type is discord.ChannelType.private):
            if DM_WEBHOOK != "":
                try:
                    webhook = Webhook.from_url(DM_WEBHOOK, adapter=RequestsWebhookAdapter())
                    embed = discord.Embed(title="Received DM", color=0xC98FFC)
                    embed.add_field(name="User:",value=message.author,inline=False)
                    embed.add_field(name="User ID:",value=message.author.id,inline=False)
                    est = timezone('EST')
                    time= datetime.now(est)
                    hour = int(time.strftime("%H")) + 1
                    embed.add_field(name="Received:",value=time.strftime(f"%A, %B %d %Y @ {hour}:%M %p EST"),inline=False)
                    embed.set_thumbnail(url="https://i.imgur.com/sKwqOXE.png")
                    embed.set_footer(text="BingBot Self-Bot", icon_url="https://i.imgur.com/sKwqOXE.png")
                    song("dm")
                    print(f"Received Direct Message: {message.author}")
                    webhook.send(embed=embed)
                except:
                    pass

    @bing.command()
    async def commands(ctx):
        with open ("commands.json", "r") as f:
            data = json.load(f)
        commands_list = list(data.keys())
        commands_str = "\n".join(commands_list)
        if EMBED_MODE.lower() == "on":
            embed = discord_self_embed.Embed("Available Commands:",description=commands_str,colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
            embed.set_author(ctx.author.display_name)
            url = embed.generate_url(hide_url=True)
            await ctx.send(url)
        else:
            await ctx.send(f"```\n\tAvailable Commands:\n{commands_str}\n```")

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
        if EMBED_MODE.lower() == "on":
            embed = discord_self_embed.Embed(f"You have deleted {messagesdeleted} messages",colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
            url = embed.generate_url(hide_url=True)
            await ctx.send(url)
        else:
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
            if EMBED_MODE.lower() == "on":
                embed = discord_self_embed.Embed(f"{name}'s Hypixel Statistics",description="Hypixel Rank: {}\nKarma: {:,}\nNetwork XP: {:,.2f}\nHypixel Level: {:.2f}".format(rank, data['player']['karma'], data['player']['networkExp'], level),colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                url = embed.generate_url(hide_url=True)
                await ctx.send(f"{url}\nhttps://crafatar.com/renders/body/{uuid}")
            else:
                await ctx.send("```\n\t\t{}'s Hypixel Statistics:\nHypixel Rank: {}\nKarma: {:,}\nNetwork XP: {:,.2f}\nHypixel Level: {:.2f}\n```\nhttps://crafatar.com/renders/body/{}".format(name, rank, data['player']['karma'], data['player']['networkExp'], level, uuid))
        except:
            if EMBED_MODE.lower() == "on":
                embed = discord_self_embed.Embed(f"Error: Invalid IGN or API Key",colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                url = embed.generate_url(hide_url=True)
                await ctx.send(url)
            else:
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
                
                if EMBED_MODE.lower() == "on":
                    embed = discord_self_embed.Embed(f"{name}'s Skyblock Statistics",description="Active Profile: {}\nSkill Average: {:,.1f}\nFarming: {:.0f}\nMining: {:.0f}\nCombat: {:.0f}\nForaging: {:.0f}\nFishing: {:.0f}\nEnchanting: {:.0f}\nAlchemy: {:.0f}\nTaming: {:.0f}".format(profile_name,skill_average(),farming(),mining(),combat(),foraging(),fishing(),enchanting(),alchemy(),taming()),colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                    url = embed.generate_url(hide_url=True)
                    await ctx.send(f"{url}")
                else:
                    await ctx.send("```\n\t\t{}'s Skyblock Skills:\nActive Profile: {}\nSkill Average: {:,.1f}\nFarming: {:.0f}\nMining: {:.0f}\nCombat: {:.0f}\nForaging: {:.0f}\nFishing: {:.0f}\nEnchanting: {:.0f}\nAlchemy: {:.0f}\nTaming: {:.0f}\n```".format(name,profile_name,skill_average(),farming(),mining(),combat(),foraging(),fishing(),enchanting(),alchemy(),taming()))
            except:
                if EMBED_MODE.lower() == "on":
                    embed = discord_self_embed.Embed(f"Error: Invalid IGN or API Key",colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                    url = embed.generate_url(hide_url=True)
                    await ctx.send(url)
                else:
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

                if EMBED_MODE.lower() == "on":
                    embed = discord_self_embed.Embed(f"{name}'s Skyblock Statistics",description="Active Profile: {}\nWeight: {:,.2f}\nOverflow Weight: {:,.2f}\nTotal Weight: {:,.2f}".format(profile_name,weight(),overflow(),total_weight()),colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                    url = embed.generate_url(hide_url=True)
                    await ctx.send(f"{url}")
                else:
                    await ctx.send("```\n\t\t{}'s Skyblock Weight:\nActive Profile: {}\nWeight: {:,.2f}\nOverflow Weight: {:,.2f}\nTotal Weight: {:,.2f}\n```".format(name,profile_name,weight(),overflow(),total_weight()))
            except:
                if EMBED_MODE.lower() == "on":
                    embed = discord_self_embed.Embed(f"Error: Invalid IGN or API Key",colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                    url = embed.generate_url(hide_url=True)
                    await ctx.send(url)
                else:
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
                senither = f"https://hypixel-api.senither.com/v1/profiles/{uuid}?key={API_KEY}"
                senither_data = getInfo(senither)
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

                SPIDER_XP = senither_data['data'][profile_num]['slayers']['bosses']['tarantula']['experience']
                SPIDER_LVL = senither_data['data'][profile_num]['slayers']['bosses']['tarantula']['level']
                REV_XP = senither_data['data'][profile_num]['slayers']['bosses']['revenant']['experience']
                REV_LVL = senither_data['data'][profile_num]['slayers']['bosses']['revenant']['level']
                SVEN_XP = senither_data['data'][profile_num]['slayers']['bosses']['sven']['experience']
                SVEN_LVL = senither_data['data'][profile_num]['slayers']['bosses']['sven']['level']
                ENDER_XP = senither_data['data'][profile_num]['slayers']['bosses']['enderman']['experience']
                ENDER_LVL = senither_data['data'][profile_num]['slayers']['bosses']['enderman']['level']
                COINS_SPENT = senither_data['data'][profile_num]['slayers']['total_coins_spent']

                if EMBED_MODE.lower() == "on":
                    embed = discord_self_embed.Embed(f"{name}'s Slayer XP and Levels",description="Active profile: {}\nTotal Coins Spent: {:.0f}\n\nRevenant Horror: Level {}\nSlayer XP {:,.0f}\n\nTarantula Broodfather: Level {}\nSlayer XP {:,.0f}\n\nSven Packmaster: Level {}\nSlayer XP {:,.0f}\n\nVoidgloom Seraph: Level {}\nSlayer XP {:,.0f}".format(profile_name, COINS_SPENT, REV_LVL, REV_XP, SPIDER_LVL, SPIDER_XP, SVEN_LVL, SVEN_XP, ENDER_LVL, ENDER_XP),colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                    url = embed.generate_url(hide_url=True)
                    await ctx.send(f"{url}")
                else:
                    await ctx.send("```\n\t\t{}'s Slayer XP and Levels\nActive profile: {}\nTotal Coins Spent: {:.0f}\n\nRevenant Horror: Level {}\nSlayer XP {:,.0f}\n\nTarantula Broodfather: Level {}\nSlayer XP {:,.0f}\n\nSven Packmaster: Level {}\nSlayer XP {:,.0f}\n\nVoidgloom Seraph: Level {}\nSlayer XP {:,.0f}\n```".format(name, profile_name, COINS_SPENT, REV_LVL, REV_XP, SPIDER_LVL, SPIDER_XP, SVEN_LVL, SVEN_XP, ENDER_LVL, ENDER_XP))
            except:
                if EMBED_MODE.lower() == "on":
                    embed = discord_self_embed.Embed(f"Error: Invalid IGN or API Key",colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                    url = embed.generate_url(hide_url=True)
                    await ctx.send(url)
                else:
                    await ctx.send("```\nError:\nInvalid IGN\n```")
        else:
            await ctx.send("`Invalid API Key`")
    
    @bing.command()
    async def embed(ctx, url="https://github.com/itsb1ng/BingBot-Self-Bot", *, title="BingBot Self-Bot"):
        if "https" not in url or "http" not in url:
            url = "https://github.com/itsb1ng/BingBot-Self-Bot"
        embed = discord_self_embed.Embed(title, colour="C98FFC", url=url)
        embed_send = embed.generate_url(hide_url=True)
        await ctx.send(embed_send)

    @bing.command()
    async def pets(ctx, name):
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

                PETS_LIST = []
                if len(senither_data['data'][profile_num]['pets']) > 0:
                    if EMBED_MODE.lower() == "on":
                        for pet in range(0,10):
                            PET = "{} {} (LVL {:.0f})".format(senither_data['data'][profile_num]['pets'][pet]['tier'],senither_data['data'][profile_num]['pets'][pet]['type'],senither_data['data'][profile_num]['pets'][pet]['level'])
                            PETS_LIST.append(PET)
                    else:
                        for pet in range(len(senither_data['data'][profile_num]['pets'])):
                            PET = "{} {} (LVL {:.0f})".format(senither_data['data'][profile_num]['pets'][pet]['tier'],senither_data['data'][profile_num]['pets'][pet]['type'],senither_data['data'][profile_num]['pets'][pet]['level'])
                            PETS_LIST.append(PET)
                    ALL_PETS = "\n".join(PETS_LIST)

                    if EMBED_MODE.lower() == "on":
                        embed = discord_self_embed.Embed(f"{name}'s Skyblock Pets",description="Active Profile: {}\n\n{}".format(profile_name, ALL_PETS),colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                        url = embed.generate_url(hide_url=True)
                        await ctx.send(f"{url}")
                    else:
                        await ctx.send("```\n\t\t{}'s Skyblock Pets:\nActive Profile: {}\n\n{}```".format(name,profile_name, ALL_PETS))
                else:
                    if EMBED_MODE.lower() == "on":
                        embed = discord_self_embed.Embed(f"{name} has no pets",description=f"Recent profile ({profile_name}) states user has no pets",colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                        url = embed.generate_url(hide_url=True)
                        await ctx.send(f"{url}")
                    else:
                        await ctx.send(f"```{name} has no pets\nRecent profile ({profile_name}) states user has no pets```")
            except:
                if EMBED_MODE.lower() == "on":
                    embed = discord_self_embed.Embed(f"Error: Invalid IGN or API Key",colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                    url = embed.generate_url(hide_url=True)
                    await ctx.send(url)
                else:
                    await ctx.send("```\nError:\nInvalid IGN\n```")
        else:
            await ctx.send("`Invalid API Key`")

    @bing.command()
    async def nitro(ctx, option):
        try:
            if option.lower() == "on" or option.lower() == "off":
                if option.lower() == "on" and config[1]['nitro'].lower() == "off":
                    config.pop(1)
                    decision = "on"
                    decision_dict = {"nitro": "on"}
                    regular_dict = config[0]
                    dict_list = [regular_dict, decision_dict]
                    out_file = open("config.json", "w")
                    json.dump(dict_list, out_file)
                    out_file.close()
                    await ctx.send(f"`Nitro Sniper is now {decision}, BingBot Self-Bot will now restart`")
                    bing_restart()
                elif option.lower() == "off" and config[1]['nitro'].lower() == "on":
                    config.pop(1)
                    decision = "off"
                    decision_dict = {"nitro": "off"}
                    regular_dict = config[0]
                    dict_list = [regular_dict, decision_dict]
                    out_file = open("config.json", "w")
                    json.dump(dict_list, out_file)
                    out_file.close()
                    await ctx.send(f"`Nitro Sniper is now {decision}, BingBot Self-Bot will now restart`")
                    bing_restart()
                else:
                    await ctx.send(f"`Nitro Sniper is already {option.lower()}`")
            else:
                await ctx.send("`Invalid Enry!`")
        except:
            await ctx.send("`Invalid Enry!`")

    @bing.command()
    async def restart(ctx):
        try:
            await ctx.send("`BingBot Self-Bot is now restarting`")
            bing_restart()
        except:
            pass

    @bing.command()
    async def playerdiscord(ctx, ign):
        try:
            user_name = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}").json()
            link = f"https://api.slothpixel.me/api/players/{ign}"
            data = getInfo(link)
            user_discord = data['links']['DISCORD']

            if EMBED_MODE.lower() == "on":
                embed = discord_self_embed.Embed(f"{user_name['name']}",description=f"Discord: {user_discord}", colour="C98FFC",url="https://github.com/itsb1ng/BingBot-Self-Bot")
                url = embed.generate_url(hide_url=True)
                await ctx.send(url)
            else:
                await ctx.send(f"```\n\t\t{user_name['name']}\nDiscord: {user_discord}\n```")
        except:
            await ctx.send("`Invalid Enry!`")

    @bing.command()
    async def spamwebhook(ctx, webber, num="25"):
        try:
            webber_json = requests.get(webber).json()
            webhook = Webhook.from_url(webber, adapter=RequestsWebhookAdapter())
            MSG_LINK = "https://gaming-at-my.best/watch.php?video=4V051I.mp4"
            embed = discord.Embed(title="ShitRatter.mp4", url=MSG_LINK,color=0xC98FFC)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/953054084833878066/953843770456150026/IMG_0672.jpg")
            embed.add_field(name="Use better obfuscation next time retard", value="Get beamed bitch")
            await ctx.send(f"`{webber_json['name']} is now getting spammed`")
            for x in range(0,int(num)):
                webhook.send(username="BingBot On Top",avatar_url="https://i.imgur.com/sKwqOXE.png",embed=embed)
                time.sleep(2)
        except:
            await ctx.send("`Could not spam webhook`")

    @bing.command()
    async def deletewebhook(ctx, webber):
        try:
            webber_json = requests.get(webber).json()
            await ctx.send(f"`{webber_json['name']} has been nuked`")
            os.system(f"curl -X DELETE {webber}")
        except:
            await ctx.send("`Webhook has already been nuked`")

    startup(config[0]['startup'])
    bing.run(DISCORD_TOKEN)
except:
    song("failedlogin")
    print("\nInvalid Discord Token\n")