import os

import discord

token = os.environ["TOKEN"]
shift = 32
words = ["amogus", "sussy", "baka", "impostor", "amogsus", "sugondese", "daddy", "submissive", "breedable"]
translations = ["mog"]
for word in words:
    for start in range(len(word)):
        for end in range(start + 3, len(word) + 1):
            part = word[start:end]
            if part in translations:
                continue
            translations.append(part)

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
    if message.content.startswith("ඞtoamog"):
        for char in message:
            index = ord(char) - shift
            if char == ' ':
                index = 0
            if index >= len(translations):
                message += translations[63 - shift]
                continue
            response += translations[index]
    elif message.content.startswith("ඞfromamog"):
        parts = message.split(" ")
        for message_part in parts:
            for i, match in enumerate(translations):
                if message_part == match:
                    if i == 0:
                        response += " "
                    response += chr(i + shift)
                    break
                response += "?"
    await message.channel.send(response)
    client.run(token)
