import asyncio
import random

import nextcord
from nextcord.ext import commands
from pymongo import MongoClient

Client = MongoClient(
    "MONGO_DB_URI"
)
Collections = Client["BarbotDB"]
db = Collections["economydb"]
cooldown = Collections["cooldowns"]


class EconomyApp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Check your balance!")
    async def balance(self, ctx: nextcord.Interaction, member: nextcord.User = None):
        if not member:
            member = ctx.user

        get_bank_info = db.find_one({"userid": member.id})
        if get_bank_info is not None:
            e = nextcord.Embed(title=f"{member}'s Balance")
            e.add_field(name="Wallet", value=get_bank_info["money"])
            e.add_field(name="Bank", value=get_bank_info["bank"])
            await ctx.response.send_message(embed=e)
        else:
            db.insert_one(
                {"user": member.name, "userid": member.id, "money": 0, "bank": 0}
            )
            get_new_info = db.find_one({"userid": member.id})
            e = nextcord.Embed(title=f"{member.name}'s Balance")
            e.add_field(name="Wallet", value=get_new_info["money"])
            e.add_field(name="Bank", value=get_new_info["bank"])
            await ctx.response.send_message(embed=e)

    @nextcord.slash_command(description="Work and get some money!")
    async def work(self, ctx: nextcord.Interaction):
        check = cooldown.find_one({"userid": ctx.user.id})
        if check is None:
            get_bank_info = db.find_one({"userid": ctx.user.id})
            if get_bank_info:
                generate_money = random.randint(15, 130)
                income = generate_money
                update_user = get_bank_info["money"] + income
                db.update_one({"userid": ctx.user.id}, {"$set": {"money": update_user}})
                await ctx.response.send_message(
                    f"You worked and got `{income}$` in return."
                )
            else:
                db.insert_one(
                    {
                        "user": ctx.user.name,
                        "userid": ctx.user.id,
                        "money": 0,
                        "bank": 0,
                    }
                )
                generate_money = random.randint(15, 130)
                get_new_info = db.find_one({"userid": ctx.user.id})
                update_user = get_new_info["money"] + generate_money
                db.update_one({"userid": ctx.user.id}, {"$set": {"money": update_user}})
                await ctx.response.send_message(
                    f"You worked and got `{generate_money}$` in return."
                )
                cooldown.insert_one({"userid": ctx.user.id})
                await asyncio.sleep(1800)
                cooldown.delete_one({"userid": ctx.user.id})
        else:
            await ctx.response.send_message("Hey! Slowdown your on a cooldown here!")

    @nextcord.slash_command(description="Deposit some money to your bank!")
    async def deposit(self, ctx: nextcord.Interaction, amount: int = None):
        get_bank_info = db.find_one({"userid": ctx.user.id})
        if get_bank_info:
            money = get_bank_info["money"]
            bank = get_bank_info["bank"]

            if amount > money:
                return await ctx.response.send_message(
                    "You dont have that much money to deposit!"
                )
            elif amount < 0:
                return await ctx.response.send_message("Wait... That's illegal!")
            else:
                update_money = money - amount
                update_bank = bank + amount
                db.update_one(
                    {"userid": ctx.user.id}, {"$set": {"money": update_money}}
                )
                db.update_one({"userid": ctx.user.id}, {"$set": {"bank": update_bank}})
                await ctx.response.send_message("Transaction Complete!")
        else:
            db.insert_one(
                {
                    "user": ctx.user.name,
                    "userid": ctx.user.id,
                    "money": 0,
                    "bank": 0,
                }
            )
            await ctx.response.send_message(
                "You dont have that much money to withdraw!"
            )

    @nextcord.slash_command(description="Withdraw some money from your bank!")
    async def withdraw(self, ctx: nextcord.Interaction, amount: int = None):
        get_bank_info = db.find_one({"userid": ctx.user.id})
        if get_bank_info:
            money = get_bank_info["money"]
            bank = get_bank_info["bank"]

            if amount > bank:
                return await ctx.response.send_message(
                    "You dont have that much money to withdraw!"
                )
            elif amount < 0:
                return await ctx.response.send_message("Wait... That's illegal!")
            else:
                update_money = money + amount
                update_bank = bank - amount
                db.update_one(
                    {"userid": ctx.user.id}, {"$set": {"money": update_money}}
                )
                db.update_one({"userid": ctx.user.id}, {"$set": {"bank": update_bank}})
                await ctx.response.send_message("Transaction Complete!")
        else:
            db.insert_one(
                {
                    "user": ctx.user.name,
                    "userid": ctx.user.id,
                    "money": 0,
                    "bank": 0,
                }
            )
            await ctx.response.send_message(
                "You dont have that much money to withdraw!"
            )

    @nextcord.slash_command(description="Send money to your buddies!")
    async def send(
        self, ctx: nextcord.Interaction, amount: int, *, member: nextcord.Member
    ):
        if member.id == ctx.user.id:
            return await ctx.response.send_message(
                "Wait... Why are you sending money to yourself?"
            )
        else:
            get_sender = db.find_one({"userid": ctx.user.id})
            get_receiver = db.find_one({"userid": member.id})

            if get_receiver and get_sender:
                if amount > get_sender["money"]:
                    return await ctx.response.send_message(
                        "You dont have that much money to give!"
                    )
                elif amount < 0:
                    return await ctx.response.send_message("Wait... That's illegal!")
                else:
                    update_sender = get_sender["money"] - amount
                    update_receiver = get_receiver["money"] + amount
                    db.update_one(
                        {"userid": ctx.user.id}, {"$set": {"money": update_sender}}
                    )
                    db.update_one(
                        {"userid": ctx.user.id}, {"$set": {"bank": update_receiver}}
                    )
                    await ctx.response.send_message("Transaction Complete!")

            elif get_sender is None:
                db.insert_one(
                    {
                        "user": ctx.user.name,
                        "userid": ctx.user.id,
                        "money": 0,
                        "bank": 0,
                    }
                )
                return await ctx.response.send_message(
                    "You cant give that amount of money!"
                )

            elif get_receiver is None:
                db.insert_one(
                    {
                        "user": ctx.user.name,
                        "userid": ctx.user.id,
                        "money": 0,
                        "bank": 0,
                    }
                )

                if amount > get_sender["money"]:
                    return await ctx.response.send_message(
                        "You dont have that much money to give!"
                    )
                elif amount < 0:
                    return await ctx.response.send_message("Wait... That's illegal!")
                else:
                    update_sender = get_sender["money"] - amount
                    update_receiver = get_receiver["money"] + amount
                    db.update_one(
                        {"userid": ctx.user.id}, {"$set": {"money": update_sender}}
                    )
                    db.update_one(
                        {"userid": ctx.user.id}, {"$set": {"bank": update_receiver}}
                    )
                    await ctx.response.send_message("Transaction Complete!")


def setup(bot):
    bot.add_cog(EconomyApp(bot))
