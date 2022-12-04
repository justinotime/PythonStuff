import discord
import discord

# create Client object - the bot itself
client = discord.Client(intents=discord.Intents.all())  # intents: don't worry about it!

# decorator to register an event for the bot to listen to
@client.event
async def on_ready():  # on_ready() event: when bot is ready!
    print(f'{client.user} has connected to Discord!')

# your Discord token goes here
DISCORD_TOKEN = "MTA0MzI4ODIzNjA3MzY5NzMzNA.GAaazP.x8y3-7qRDoyJPWZlJ8Tk-Eq6Wuhn1B-KohEX-Q"   
client.run(DISCORD_TOKEN)  # .run() -> to run the bot

# https://discord.gg/eCKmRc5h(link to the workshop/discord)
# Bot token: MTA0MzI4ODIzNjA3MzY5NzMzNA.GAaazP.x8y3-7qRDoyJPWZlJ8Tk-Eq6Wuhn1B-KohEX-Q