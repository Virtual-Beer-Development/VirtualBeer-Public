import nextcord
from nextcord.ext import commands
from pymongo import MongoClient

Client = MongoClient(
    "MONGO_DB_URI"
)
Collections = Client["BarbotDB"]
db = Collections["blacklistdb"]


class Blacklist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def ban(self, ctx, user: nextcord.User, *, reason):
        if not user:
            return await ctx.send("Please mention a member!")
        else:
            check_blacklist = db.find_one({"userid": user.id})
            if check_blacklist:
                db.insert_one({"userid": user.id, "reason": reason})
                await ctx.send(f"`{user.id}` Has been blacklisted.")
            else:
                await ctx.send("This user is already blacklisted.")


def setup(bot):
    bot.add_cog(Blacklist(bot))
