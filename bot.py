import discord
from discord.ext import commands
from discord.ext.commands import is_owner
import os

prefix: str = "$"

intents = discord.Intents.default()
intents.message_content = True

#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'We have logged in as {bot.user}')


@bot.hybrid_command(name='ping', description='Ping the bot')
async def ping(interaction: discord.Interaction):
    await interaction.channel.send("Pong!")


@bot.hybrid_command(name='sync', description='Developer only. Syncs command tree')
@is_owner()
async def sync(interaction: discord.Interaction) -> None:
    output: str = ""
    synced = await bot.tree.sync()

    output = f"{len(synced)} commands synced:\n"

    for i in synced:
        output += (f"- {i.name}\n")

    await interaction.response.send_message(output)


bot.run(os.environ['CASINOBOT_DISCORD_TOKEN'])

