import nextcord
import time
from nextcord.ext import commands


class YesNoUI(nextcord.ui.View):
    def __init__(self, bot, error):
        self.bot = bot
        self.error = error
        super().__init__()

    @nextcord.ui.button(style=nextcord.ButtonStyle.green, custom_id="Yes", label="Yes")
    async def Yes(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        fatal_yes_logs = self.bot.get_channel(1061608889637949480)
        e = nextcord.Embed(
            title=f"Fatal Error! | {interaction.user} - {interaction.user.id} | {interaction.guild.name} - {interaction.guild_id}",
            description=f"```py\n{self.error}```",
            color=nextcord.Color.red(),
        )
        await fatal_yes_logs.send(embed=e)

        eH = nextcord.Embed(
            title="Crash Report sent!",
            description="Thank you for letting us get a report! This will let us server the issue at the earliest! ",
            color=nextcord.Color.green(),
        )

        await interaction.response.send_message(embed=eH)
        return self.stop()

    @nextcord.ui.button(style=nextcord.ButtonStyle.red, custom_id="No", label="No")
    async def No(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        e = nextcord.Embed(
            title="Crash Report not sent!",
            description="Okay! We will not be sending the crash report to the developers. If you encounter this error again, you are free to drop us a message!",
            color=nextcord.Color.random(),
        )
        await interaction.response.send_message(embed=e)
        return self.stop()


class OnError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You are missing a required argument.")
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f"Hey! Slow down there. Your on cooldown for <t:{int(time.time() + error.retry_after)}:R>"
            )
        else:
            eH = nextcord.Embed(
                title="We encountered an error!",
                description=f"The error was as follows:\n ```py\n{error}``` ",
                color=nextcord.Color.red(),
            )

            eH.set_footer(
                text=f"On clicking Yes, your username, user ID, server name and the server ID where the error was encountered will be sent."
            )

            view = YesNoUI(self.bot, error)
            await ctx.send(embed=eH, view=view)


def setup(bot):
    bot.add_cog(OnError(bot))
