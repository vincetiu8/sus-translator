import os
import random

import discord

shift = 32
words = ["amogus", "sussy", "baka", "impostor", "amogsus", "sugondese", "daddy", "submissive", "breedable"]
translations = []
for word in words:
    for start in range(len(word)):
        for end in range(start + 3, len(word) + 1):
            part = word[start:end]
            if part in translations:
                continue
            translations.append(part)

random.shuffle(translations)
translations.remove("amogus")
translations.insert(0, "amogus")

max_char = len(translations)

client = discord.Client()


@client.event
async def on_ready():
    print("The sus has arrived ඞඞඞ")


@client.event
async def on_message(message):
    if message.author == client.user or not message.content.startswith("ඞ"):
        return

    response = "ඞඞඞ Your translation is: "
    if message.content.startswith("ඞtoamog "):
        for char in message.content.split("ඞtoamog ")[1]:
            index = ord(char) - shift
            if char == ' ':
                index = 0
            if index >= len(translations):
                response += translations[63 - shift] + " "
                continue
            response += translations[index] + " "
    elif message.content.startswith("ඞfromamog "):
        parts = message.content.split("ඞfromamog ")[1].split(" ")
        for message_part in parts:
            for i, match in enumerate(translations):
                if message_part == match:
                    if i == 0:
                        response += " "
                    else:
                        response += chr(i + shift)
                    break
            else:
                response += "?"
    else:
        response = "Invalid command, you sussy baka ඞඞඞ"

    await message.channel.send(response)


client.run(os.getenv("TOKEN"))
