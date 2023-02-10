import random
import nextcord
from nextcord.ext import commands


class Eightball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball")
    async def eightball(self, ctx, *, question=None):
        if question is None:
            return await ctx.send("Whats your question dummy!")
        else:
            responses = [
                "No, Im not a wizard.",
                "Yea, Maybe sure...",
                "How about you give me a cookie.",
                "Oh yea ofc, No.",
                "Maybe yea.",
                "Im giving you 5 seconds to take that back.",
            ]
            res = random.choice(responses)

            e = nextcord.Embed(title="🎱 The Ball Has Spoken 🎱", description=responses)
            await ctx.send(embed=e)

    @commands.command()
    async def coin(self, ctx):
        chances = [0, 1]
        choice = random.choice(chances)

        if choice == 0:
            await ctx.send("The coin has landed on... **`Tails`** ✨")
        else:
            await ctx.send("The coin has landed on... **`Heads`** ✨")


def setup(bot):
    bot.add_cog(Eightball(bot))
