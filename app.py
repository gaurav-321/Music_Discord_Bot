import asyncio
import time

import discord
from discord.ext import commands

from functions import get_music

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


class Queue():
    def __init__(self):
        self.data = {}
        self.skip = {}
        for guild in bot.guilds:
            self.data[guild.name] = []
        for guild in bot.guilds:
            self.skip[guild.name] = False

    def add_music(self, guild_name, music):
        if guild_name not in self.data.keys():
            self.data[guild_name] = [music]
        else:
            self.data[guild_name].append(music)

    def clear_queue(self, guild_name):
        self.data[guild_name] = []

    def music_done(self, guild_name):
        self.data[guild_name].pop(0)

    def add_skip(self, guild_name):
        self.skip[guild_name] = True

    def check_skip(self, guild_name):
        return self.skip[guild_name]


def create_embed(data):
    data = data
    embed = (discord.Embed(title='Now playing',
                           description=data["title"],
                           color=discord.Color.blurple()).add_field(name='Duration', value=data['duration'])
             .add_field(name='Uploader', value=data['channel'])
             .add_field(name='URL', value=data['link'])
             .set_thumbnail(url=data['thumbnail']))

    return embed


queue = Queue()


@bot.event
async def on_ready():
    global queue
    queue = Queue()


@bot.command(name='play', help='Plays a song')
async def play_music(ctx, *args):
    voice_channel = ctx.message.author.voice.channel
    # Check if the user is connected to a voice channel
    if voice_channel is not None:
        # Check if the bot is already playing a song
        if len(args) == 0:
            await ctx.send('Please enter a song name')
        else:
            try:
                if ctx.voice_client.is_playing():
                    queue.add_music(ctx.guild.name, " ".join(args))
                    await ctx.send(f'**Added to queue:** {" ".join(args)}')
                    return True
            except Exception as e:
                print(e)
            queue.add_music(ctx.guild.name, " ".join(args))
            vc = await voice_channel.connect()
            while len(queue.data[ctx.guild.name]) > 0:
                if ctx.voice_client is None:
                    vc = await voice_channel.connect()
                music_details = get_music(queue.data[ctx.guild.name][0])
                await ctx.send(embed=create_embed(music_details))
                vc.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=music_details['file']))
                while ctx.voice_client and ctx.voice_client.is_playing():
                    await asyncio.sleep(1)
                time.sleep(3)
                queue.music_done(ctx.guild.name)
            await ctx.send('**Queue is empty.**')
            await vc.disconnect()
    else:
        await ctx.send('**You are not connected to a voice channel.**')


@bot.command(name='skip', help='Skips current song')
async def skip(ctx, *args):
    try:
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send(':fast_forward: **Skipping current song.**')
    except:
        await ctx.send(':x: **No music is playing.**')


@bot.command(name='emptyqueue', help='Empties the queue')
async def empty_queue(ctx, *args):
    queue.clear_queue(ctx.guild.name)
    await ctx.send(':wastebasket: **Queue has been emptied.**')


@bot.command(name='stop', help='Stops the bot')
async def stop(ctx, *args):
    try:
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send(':stop_button: **Stopping current music.**')
    except:
        await ctx.send(':x: **No music is playing.**')
    try:
        await ctx.voice_client.disconnect()
        await ctx.send(':wave: **Disconnected from voice channel.**')
    except:
        pass


@bot.command(name='listqueue', help='Lists the queue')
async def list_queue(ctx, *args):
    embed = discord.Embed(title='Queue', description='List of songs in queue', color=discord.Color.blurple())
    for i in range(len(queue.data[ctx.guild.name])):
        embed.add_field(name=f'Song {i + 1}', value=queue.data[ctx.guild.name][i], inline=False)
    await ctx.send(embed=embed)


@bot.command(name='helpy', help='Shows help')
async def help(ctx, *args):
    embed = discord.Embed(title='Help', description='List of commands', color=discord.Color.blurple())
    embed.add_field(name='/play', value='Plays a song', inline=False)
    embed.add_field(name='/skip', value='Skips current song', inline=False)
    embed.add_field(name='/emptyqueue', value='Empties the queue', inline=False)
    embed.add_field(name='/stop', value='Stops the bot', inline=False)
    embed.add_field(name='/help', value='Shows help', inline=False)
    await ctx.send(embed=embed)


bot.run('Use Your Token Here')
