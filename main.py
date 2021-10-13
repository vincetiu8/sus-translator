import os

import discord
from discord.ext import commands
from dislash import InteractionClient, Option, OptionType

test_guild_id = [688903458400894994]

shift = 32
words = ["mog", "og", "sus", "us", "le", "pog"]
words_len = len(words)
bot = commands.Bot(command_prefix="ඞ", help_command=None)
inter_client = InteractionClient(bot, test_guilds=test_guild_id)

move_to_front = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
translations = [chr(i) for i in range(ord("z") + 1)]
for c in move_to_front[::-1]:
    translations.remove(c)
    translations.insert(0, c)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Among Us (But in Real Life)'))


@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("ඞඞඞ The S U S has arrived ඞඞඞ\nMy prefix is ඞ, and there's no changing it sussy bakas!")


@inter_client.slash_command(
    name="toamog",
    description="Translates to amoglish",
    options=[
        Option("message", "Message to translate to amoglish", OptionType.STRING, required=True)
    ]
)
async def _toamog(ctx, message=None):
    resp = "ඞඞඞ Your translation is: "
    for i, char in enumerate(message):
        if char == " ":
            resp += " "
            continue

        if 0 < i and message[i - 1] != " ":
            resp += "a"

        try:
            index = translations.index(char)
        except:
            index = ord(char)

        if index == 0:
            resp += words[0]
            continue

        while index > 0:
            resp += words[index % words_len]
            index //= words_len
    await ctx.reply(resp)


@bot.command(name="toamog", help="Translates to amoglish")
async def to_amog_bot(ctx):
    await _toamog(ctx, ctx.message.content[8:])


@inter_client.slash_command(
    name="fromamog",
    description="Translates from amoglish",
    options=[
        Option("message", "Message to translate from amoglish", OptionType.STRING, required=True)
    ]
)
async def _fromamog(ctx, message=None):
    resp = "ඞඞඞ Your translation is: "
    parts = message.split(" ")
    for message_part in parts:
        letters = message_part.split("a")
        for letter in letters:
            index = 0
            power = 1
            while len(letter) > 0:
                for i, word in enumerate(words):
                    if letter.startswith(word):
                        index += power * i
                        power *= words_len
                        letter = letter[len(word):]
                        break
                else:
                    await ctx.reply("Not valid amoglish, you sussy baka ඞඞඞ")
                    return
            if index < len(translations):
                resp += translations[index]
                continue
            resp += chr(index)
        resp += " "
    await ctx.reply(resp)


@bot.command(name="fromamog", help="Translates from amoglish")
async def from_amog_bot(ctx):
    await _fromamog(ctx, ctx.message.content[10:])


@inter_client.slash_command(
    name="help",
    description="Get some help"
)
async def _help(ctx):
    resp = "Hey sussy baka, here are my commands:\nඞtoamog: translate to amoglish\nඞfromamog: translate from " \
           "amoglish"
    await ctx.send(resp)


@bot.command(name="help", help="Get some help")
async def help(ctx):
    await _help(ctx)


bot.run(os.getenv("TOKEN"))
