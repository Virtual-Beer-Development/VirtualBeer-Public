import nextcord
from nextcord.ext import commands
from pymongo import MongoClient

Client = MongoClient(
    "MONGO_DB_URI"
)
Collections = Client["BarbotDB"]
db = Collections["blacklistdb"]


class Unblacklist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def unban(self, ctx, user: nextcord.User, *, reason):
        if not user:
            return await ctx.send("Please mention a member!")
        else:
            check_blacklist = db.find_one({"userid": user.id})
            if check_blacklist:
                db.delete_one({"userid": user.id})
                await ctx.send(f"`{user.id}` Has been unblacklisted.")
            else:
                await ctx.send("This user is not blacklisted.")


def setup(bot):
    bot.add_cog(Unblacklist(bot))
