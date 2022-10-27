import discord

intents = discord.Intents.default()
intents.messages= True
client = discord.Client(intents=intents)
bottoken=open("C:/geheim/discordbot.txt", "r").readline()

@client.event
async def on_ready():

    guild = client.guilds[0]
    print(guild.name, "is te nae of the server")
    print(client.user, "has connected to the server")
    channel = guild.text_channels[0]
    print(channel.name, "is the name of the channel")
    await channel.send("I'm online")

@client.event
async def on_message(message):
    print(message.channel.name, "the message was posted from this channel")
    print(message.content)
    print(message.author, "is the user who wrote this")
    print(message.created_at, "is when the message was posted")
    print(message.channel, "is the channel this message was posted")
    if message.author.bot == False:
        await message.channel.send("Hello " + str(message.author))
    
    

client.run(bottoken)

