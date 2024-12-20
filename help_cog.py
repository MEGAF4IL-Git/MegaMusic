import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = ""
        self.text_channel_list = []
        self.set_message()

    def set_message(self):
        self.help_message = f"""
```
General commands:
{self.bot.command_prefix}Help - Displays all the available commands.
{self.bot.command_prefix}Q - Displays the current music queue.
{self.bot.command_prefix}P <YouTube Link> - finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused.
{self.bot.command_prefix}Skip - Skips the current song being played.
{self.bot.command_prefix}Clear - Stops the music and clears the queue.
{self.bot.command_prefix}Stop - Disconnect the bot from the voice channel.
{self.bot.command_prefix}Pause - Pauses the current song being played or resumes if already paused.
{self.bot.command_prefix}Resume - Resumes playing the current song.
{self.bot.command_prefix}Prefix - change command prefix.
{self.bot.command_prefix}Remove - Removes most recently added song from the queue.
```
"""

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(f"type {self.bot.command_prefix}help"))

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)
    
    @commands.command(name="prefix", help="Change bot prefix")
    async def prefix(self, ctx, *args):
        self.bot.command_prefix = " ".join(args)
        self.set_message()
        await ctx.send(f"prefix set to **'{self.bot.command_prefix}'**")
        await self.bot.change_presence(activity=discord.Game(f"type {self.bot.command_prefix}help"))

    @commands.command(name="send_to_all", help="send a message to all members")
    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
