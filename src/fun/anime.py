import animec
import nextcord
from nextcord.ext import commands
from animec import Waifu


class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bully(self, ctx, user: nextcord.User = None):
        if user == None:
            return await ctx.send("You cant bully yourself silly!")
        else:
            gif = Waifu.bully()
            e = nextcord.Embed(
                title=f"<@{ctx.author.name}> Bully's {user.name}",
                description="Remember, Dont bully people kids!",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await ctx.send(embed=e)

    @commands.command()
    async def cuddle(self, ctx, user: nextcord.User = None):
        if user == None:
            return await ctx.send("You cant cuddle yourself silly!")
        else:
            gif = Waifu.cuddle()
            e = nextcord.Embed(
                title=f"{ctx.author.name} Cuddles {user.name}!",
                description="Omg! So cute to see these two cuddle!",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await ctx.send(embed=e)

    @commands.command()
    async def cry(self, ctx):
        gif = Waifu.cry()
        e = nextcord.Embed(
            title=f"{ctx.author.name} Is Crying!",
            description="Aww, Dont cry...",
            color=nextcord.Color.blue(),
        )
        e.set_image(url=gif)
        await ctx.send(embed=e)

    @commands.command()
    async def hug(self, ctx, user: nextcord.User = None):
        if user == None:
            return await ctx.send("You cant hug yourself silly!")
        else:
            gif = Waifu.hug()
            e = nextcord.Embed(
                title=f"{ctx.author.name} Gave Hugs To {user.name}!",
                description="Give me a hug too! :C",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await ctx.send(embed=e)

    @commands.command()
    async def pat(self, ctx, user: nextcord.User = None):
        if user == None:
            return await ctx.send("You cant pat yourself silly!")
        else:
            gif = Waifu.pat()
            e = nextcord.Embed(
                title=f"{ctx.author.name} Gave Pats To {user.name}!",
                description="How cute can that be!",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await ctx.send(embed=e)

    @commands.command()
    async def slap(self, ctx, user: nextcord.User = None):
        if user == None:
            return await ctx.send("You cant slap yourself silly!")
        else:
            gif = Waifu.slap()
            e = nextcord.Embed(
                title=f"{ctx.author.name} Slapped {user.name}!",
                description="Ouch! Thats gonna leave a mark...",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await ctx.send(embed=e)

    @commands.command()
    async def kiss(self, ctx, user: nextcord.User = None):
        if user == None:
            return await ctx.send("You cant kiss yourself silly!")
        else:
            gif = Waifu.kiss()
            e = nextcord.Embed(
                title=f"{ctx.author.name} Kissed {user.name}!",
                description="Mazel Tov! 🙌",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await ctx.send(embed=e)

    @commands.command()
    async def poke(self, ctx, user: nextcord.User = None):
        if user == None:
            return await ctx.send("You cant hug yourself silly!")
        else:
            gif = Waifu.poke()
            e = nextcord.Embed(
                title=f"{ctx.author.name} Poked {user.name}!",
                description="Boop Boop Boop!",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Anime(bot))
