import os
import discord

from dotenv import load_dotenv
from discord.ext import commands
from gtts import gTTS

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='|')

@bot.event
async def on_ready():
    print(f'{bot.user} successfully connected to Discord.')

@bot.command(name='join', help='Make me join your Voice Chat channel!')
async def join(ctx):
    vc = ctx.voice_client
    if not vc:
        vc = ctx.author.voice.channel
        await vc.connect()
        await ctx.send(f'Connected to the {vc} vc!')
        return


@bot.command(name='s', help='Activate text-to-speech and let the bot speak for you.')
async def s(ctx, *, text=None):
    if not text:
        await ctx.send(f'Ao {ctx.author.mention}, give me something to say first!')
        return

    vc = ctx.voice_client
    if not vc:
        await ctx.send("Connect me in a voice channel first using the |join command!")
        return

    tts = gTTS(text=text, lang="it")
    tts.save("msg.mp3")

    try:
        vc.play(discord.FFmpegPCMAudio('msg.mp3'), after=lambda e: print(f"Finished playing: {e}"))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1
    finally:
        return

@bot.command(name='bb', help='Make me leave from the Voice Chat.')
async def bb(ctx):
    vc = ctx.voice_client

    if not vc:
        await ctx.send("I'm not in a voice channel!")
        return

    await vc.disconnect()
    await ctx.send("I have left the voice channel, bb")


bot.run(TOKEN)
