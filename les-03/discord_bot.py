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

client.run(bottoken)

