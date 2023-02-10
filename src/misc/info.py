import nextcord
import datetime, time
from nextcord.ext import commands
from pymongo import MongoClient

Client = MongoClient(
    "MONGO_DB_URI"
)
Collections = Client["BarbotDB"]
db = Collections["blacklistdb"]

start_time = time.time()

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rules(self, ctx):
        e = nextcord.Embed(
            title="Virtual Beer Rules",
            description="""
                           `1` You are not allowed to order anything that contains the folllowing: Sexual, Weapons, Illegal Items, Non drinkable items along with non eatable items.
                           `2` You have full control over your data, We do not share data we collect to any other companies.
                           `3` Using automated tools to exploit the bot is not allowed.
                           `4` Bypassing bans with alt accounts are not allowed.
                           `5` Using common sense while using the bot, Just because it isnt in the rules it doesnt mean you can still do it.
                           """,
        )
        await ctx.send(embed=e)

    @commands.command()
    async def banned(self, ctx, *, user: nextcord.Member = None):
        if user == None:
            user = ctx.author

        find_user = db.find_one({"userid": user.id})

        if find_user:
            reason = find_user["reason"]
            moderator = find_user["moderator"]
            e = nextcord.Embed(
                title=f"{user} Is Banned.",
                description=f"""
                               Reason: {reason}
                               Moderator: {moderator}
                               """,
            )
            await ctx.send(embed=e)
        else:
            await ctx.send("This user is not banned.")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"**🏓 Pong! | (Took {round(self.bot.latency * 1000)}ms)**")


    @commands.command()
    async def botinfo(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        ping = round(self.bot.latency * 1000)
        servers = len(self.bot.guilds)
        members_set = set()
        for guild in self.bot.guilds:
            for member in guild.members:
                members_set.add(member)
        users = len(members_set)
        e = nextcord.Embed(
            title="Bot Info",
            description=
            f"""
            `🤖` Bot name: {self.bot.user}
            `🕙` Uptime: `{text}`
            `📶` Ping: {ping}ms
            `👥` Servers: `{servers}`
            `👤` Users: `{users}`
            """,
            color=nextcord.Color.blue()
        )
        e.set_footer(text=f"Requested By: {ctx.author}")
        await ctx.send(embed=e)
        

def setup(bot):
    bot.add_cog(Info(bot))
