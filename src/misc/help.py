import nextcord
from nextcord.ext import commands
from ui import dropdowns


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        emb = nextcord.Embed(
            title="Virtual Beer - *Help* ",
            description="You asked and we shall deliver! We are at your service, what would you like to know about us!",
            color=nextcord.Color.blue(),
        )

        view = dropdowns.HelpDropdownView(ctx.author.id)
        mes = await ctx.send(embed=emb, view=view)


def setup(bot):
    bot.add_cog(Help(bot))
