import nextcord
from nextcord.ext import commands
import random
from pymongo import MongoClient

Client = MongoClient(
    "MONGO_DB_URI"
)
Collections = Client["BarbotDB"]
db = Collections["economydb"]


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="balance", aliases=["bal", "acc"])
    async def balance(self, ctx, user: nextcord.User = None):
        if not user:
            user = ctx.author

        get_bank_info = db.find_one({"userid": user.id})
        if get_bank_info != None:
            e = nextcord.Embed(title=f"{user}'s Balance")
            e.add_field(name="Wallet", value=get_bank_info["money"])
            e.add_field(name="Bank", value=get_bank_info["bank"])
            await ctx.send(embed=e)
        else:
            db.insert_one({"user": user.name, "userid": user.id, "money": 0, "bank": 0})
            get_new_info = db.find_one({"userid": user.id})
            e = nextcord.Embed(title=f"{user.name}'s Balance")
            e.add_field(name="Wallet", value=get_new_info["money"])
            e.add_field(name="Bank", value=get_new_info["bank"])
            await ctx.send(embed=e)

    @commands.command(name="work", aliases=["wrk", "wor"])
    @commands.cooldown(1, 30)
    async def work(self, ctx):
        get_bank_info = db.find_one({"userid": ctx.author.id})
        if get_bank_info:
            generate_money = random.randint(15, 130)
            income = generate_money
            update_user = get_bank_info["money"] + income
            db.update_one({"userid": ctx.author.id}, {"$set": {"money": update_user}})
            await ctx.send(f"You worked and got `{income}$` in return.")
        else:
            db.insert_one(
                {
                    "user": ctx.author.name,
                    "userid": ctx.author.id,
                    "money": 0,
                    "bank": 0,
                }
            )
            get_new_info = db.find_one({"userid": ctx.author.id})
            update_user = get_new_info["money"] + generate_money
            db.update_one({"userid": ctx.author.id}, {"$set": {"money": update_user}})
            await ctx.send(f"You worked and got `{generate_money}$` in return.")

    @commands.command(name="deposit", aliases=["dep", "depo"])
    async def deposit(self, ctx, amount: int):
        get_bank_info = db.find_one({"userid": ctx.author.id})
        if get_bank_info:
            money = get_bank_info["money"]
            bank = get_bank_info["bank"]

            if amount > money:
                return await ctx.send("You dont have that much money to deposit!")
            elif amount < 0:
                return await ctx.send("Wait... Thats illegal!")
            else:
                update_money = money - amount
                update_bank = bank + amount
                db.update_one(
                    {"userid": ctx.author.id}, {"$set": {"money": update_money}}
                )
                db.update_one(
                    {"userid": ctx.author.id}, {"$set": {"bank": update_bank}}
                )
                await ctx.send("Transaction Complete!")
        else:
            db.insert_one(
                {
                    "user": ctx.author.name,
                    "userid": ctx.author.id,
                    "money": 0,
                    "bank": 0,
                }
            )
            await ctx.send("You dont have that much money to withdraw!")

    @commands.command(name="withdraw", aliases=["with", "wit"])
    async def withdraw(self, ctx, amount: int):
        get_bank_info = db.find_one({"userid": ctx.author.id})
        if get_bank_info:
            money = get_bank_info["money"]
            bank = get_bank_info["bank"]

            if amount > bank:
                return await ctx.send("You dont have that much money to withdraw!")
            elif amount < 0:
                return await ctx.send("Wait... Thats illegal!")
            else:
                update_money = money + amount
                update_bank = bank - amount
                db.update_one(
                    {"userid": ctx.author.id}, {"$set": {"money": update_money}}
                )
                db.update_one(
                    {"userid": ctx.author.id}, {"$set": {"bank": update_bank}}
                )
                await ctx.send("Transaction Complete!")
        else:
            db.insert_one(
                {
                    "user": ctx.author.name,
                    "userid": ctx.author.id,
                    "money": 0,
                    "bank": 0,
                }
            )
            await ctx.send("You dont have that much money to withdraw!")

    @commands.command()
    async def send(self, ctx, amount: int, *, user: nextcord.User):
        if user.id == ctx.author.id:
            return await ctx.send("Wait... Why are you sending money to yourself?")
        else:
            get_sender = db.find_one({"userid": ctx.author.id})
            get_reciever = db.find_one({"userid": user.id})

            if get_reciever and get_sender:
                if amount > get_sender["money"]:
                    return await ctx.send("You dont have that much money to give!")
                elif amount < 0:
                    return await ctx.send("Wait... Thats illegal!")
                else:
                    update_sender = get_sender["money"] - amount
                    update_reciever = get_reciever["money"] + amount
                    db.update_one(
                        {"userid": ctx.author.id}, {"$set": {"money": update_sender}}
                    )
                    db.update_one(
                        {"userid": user.id}, {"$set": {"bank": update_reciever}}
                    )
                    await ctx.send("Transaction Complete!")

            elif get_sender == None:
                db.insert_one(
                    {
                        "user": ctx.author.name,
                        "userid": ctx.author.id,
                        "money": 0,
                        "bank": 0,
                    }
                )
                await ctx.send("You cant give that amount of money!")

            elif get_reciever == None:
                db.insert_one(
                    {"user": user.name, "userid": user.id, "money": 0, "bank": 0}
                )

                if amount > get_sender["money"]:
                    return await ctx.send("You dont have that much money to give!")
                elif amount < 0:
                    return await ctx.send("Wait... Thats illegal!")
                else:
                    update_sender = get_sender["money"] - amount
                    update_reciever = get_reciever["money"] + amount
                    db.update_one(
                        {"userid": ctx.author.id}, {"$set": {"money": update_sender}}
                    )
                    db.update_one(
                        {"userid": user.id}, {"$set": {"bank": update_reciever}}
                    )
                    await ctx.send("Transaction Complete!")


def setup(bot):
    bot.add_cog(Economy(bot))
