import discord
from discord.ext import commands
import os

prefix = '%'
channel_id = 665269656441061407

# help_command turns off the bot's default help command so we can use our own
# self_bot ensures the bot doesn't respond to itself
bot = commands.Bot(command_prefix=prefix, help_command = None, self_bot = False)

token = 'NjcwMTA0NDA2NTE1MjUzMjY5.Xiy3-w.zXKTcoNhjyAPLLGgxowkmUmyrRE'

# import values
gm_dict={}
with open("valuesGMAX.txt", 'r') as f:
      for line in f:
        items = line.split('/')
        key, values = items[0], items[1:]
        gm_dict[key] = values

norm_dict={}
with open("values.txt", 'r') as f:
      for line in f:
        items = line.split('/')
        key, values = items[0], items[1:]
        norm_dict[key] = values

# ensures the bot only responds to messages in the channel specified above
def is_channel(channel_ids):
    def predicate(ctx):
        return ctx.message.channel.id == channel_id
    return commands.check(predicate)

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

class CaptureRate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @is_channel(channel_id)
    @commands.command()
    async def help(self, ctx):
      msg = "Enter query as `%ball [PokemonNameHere]` to get pokemon catch rates! \n"
      msg += "Enter query as `%gball [PokemonNameHere]` to get catch rates for GMaxes!"
      await ctx.author.send(msg)

    @is_channel(channel_id)
    @commands.command()
    async def ball(self, ctx, pokemon):
      pk = pokemon.capitalize()

      if pk not in norm_dict:
        msg = "You've entered an invalid pokemon, please try again."
      else:
        msg1 = f"Here are the catch rates for {pk}:\n"
        msg2 = "\n".join(map(str, norm_dict.get(pk)))
        msg3 = "\nPlease note that these values are speculative and are not guaranteed to be accurate."
        msg = msg1 + msg2 + msg3
      await ctx.send(ctx.author.mention + ' ' + msg)

    @is_channel(channel_id)
    @commands.command()
    async def gball(self, ctx, pokemon):
      pk = pokemon.capitalize()

      if pk not in gm_dict:
        msg = "You've entered an invalid GMax pokemon, please try again."
      else:
        msg1 = f"Here are the catch rates for GMax {pk}:\n"
        msg2 = "\n".join(map(str, gm_dict.get(pk)))
        msg3 = "\nPlease note that these values are speculative and are not guaranteed to be accurate."
        msg = msg1 + msg2 + msg3
      await ctx.send(ctx.author.mention + ' ' + msg)

bot.add_cog(CaptureRate(bot))

bot.run(token)