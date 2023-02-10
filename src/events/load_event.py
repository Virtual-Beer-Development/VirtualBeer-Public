import nextcord
import os
from nextcord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(
            activity=nextcord.Activity(
                type=nextcord.ActivityType.watching, name="The bar! 🍻"
            )
        )
        print("[INFO] CLIENT IS READY")
        print("[INFO] CLIENT SCRIPTS HAS BEEN LOADED SUCCESSFULLY")
        print("[INFO] CLIENT IS ONLINE.")


def setup(bot):
    bot.add_cog(Events(bot))
