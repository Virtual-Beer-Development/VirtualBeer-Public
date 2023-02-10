import nextcord
from nextcord.ext import commands
from pymongo import MongoClient

Client = MongoClient(
    "MONGO_DB_URI"
)
Collections = Client["BarbotDB"]
db = Collections["economydb"]


class Resetacc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def resetacc(self, ctx, user: nextcord.User, *, reason):
        if not user:
            return await ctx.send("Please mention a member!")
        else:
            check_acc = db.find_one({"userid": user.id})
            if check_acc:
                db.delete_one({"userid": user.id})
                db.insert_one(
                    {"user": user.name, "userid": user.id, "money": 0, "bank": 0}
                )
                await ctx.send(f"`{user.id}` Account has been reseted.")
            else:
                await ctx.send("This user does not have an account yet.")


def setup(bot):
    bot.add_cog(Resetacc(bot))
