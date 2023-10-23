import os

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from dotenv import load_dotenv

# Initialize the bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command()
async def dictionary(ctx, dictionary, word):
    dictionaries = {
        "mw": "MWScan",
        "pw": "PWGScan",
        "gra": "GRAScan"
        # Add more dictionaries and their URLs here
    }

    if dictionary.lower() not in dictionaries:
        await ctx.send("Dictionary not found.")
        return

    dicttag = dictionaries[dictionary]
    base_url = f"https://sanskrit-lexicon.uni-koeln.de/scans/{dicttag}/2020/web/webtc/getword.php"
    url = base_url + f"?key={word}&filter=roman&noLit=off&accent=yes&transLit=hk"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        extracted_text = ""
        for tag in soup.find_all("span"):
            if tag.has_attr('class'):
                classes = tag['class']
                if 'sdata' in classes:
                    tag.string = f'\033[1m{tag.text}\033[0m'  # 太字
                if 'sdata_italic_iast' in classes:
                    tag.string = f'\033[3;32m{tag.text}\033[0m'  # 斜体で緑色
            if tag.has_attr('style'):
                style = tag['style']
                if 'color' in style:
                    color = style.split('color:', 1)[1].strip(';')
                    if color == "blue":
                        tag.string = f'\033[34m{tag.text}\033[0m'  # 指定された色
                    elif color == "rgb(160,160,160)":
                        tag.string = f'\033[30m{tag.text}\033[0m'  # 指定された色
                    else:
                        tag.string = f'\033[0m{tag.text}\033[0m'  # 指定された色
            print(tag)
    

        extracted_text = soup.get_text().strip()
        chunks = [
            extracted_text[i : i + 1990] for i in range(0, len(extracted_text), 1990)
        ]

        text = f"{word} in {dictionary}:\n"
        await ctx.send(text)

        for chunk in chunks:
            await ctx.send("```ansi\n" + chunk + "\n```")
    else:
        await ctx.send(f"Failed to fetch results for {word} in {dictionary}.")


# Replace 'YOUR_TOKEN' with your bot token
load_dotenv()
TOKEN = os.environ.get("CDSD_TOKEN")
bot.run(TOKEN)
