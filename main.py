import discord
from discord.ext import commands
import music

cogs = [music]
client = commands.Bot(command_prefix='?',intents =discord.Intents.all())
for i in range(len(cogs)):
  cogs[i].setup(client)



client.run("OTE5NzQxOTg4MDM3ODUzMjQ1.YbaOeQ.0zWpow36tPvD73OZUknBpEl6afE")