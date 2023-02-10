import nextcord
import random
import string
import asyncio
from pymongo import MongoClient
from nextcord.ext import commands
from serpapi import GoogleSearch
from helpers.drink_info import get_drink_data, DrinkInfo


Client = MongoClient(
    "MONGO_DB_URI"
)
Collections = Client["BarbotDB"]
db = Collections["economydb"]
order_db = Collections["orderdb"]


class Order(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="order", description="Order something with this command!")
    async def order(self, ctx, *, item=None):
        if item == None:
            await ctx.send("Please mention an item that you would like to order.")
        else:
            get_balance = db.find_one({"userid": ctx.author.id})
            if get_balance["money"] >= 50:
                x = get_drink_data(item)
                if x == True:
                    update_money = get_balance["money"] - 50
                    db.update_one(
                        {"userid": ctx.author.id}, {"$set": {"money": update_money}}
                    )
                    params = {
                        "q": item,
                        "tbm": "isch",
                        "ijn": "0",
                        "api_key": "3f38d446535e22ea00c7a8a9f79435bb4d34f0a1d542de7c64bb97481f0385bc",
                    }
                    search = GoogleSearch(params)
                    results = search.get_dict()
                    random_search = random.randint(0, 100)
                    images_results = results["images_results"][random_search]
                    order_id = "".join(
                        (random.choice(string.ascii_lowercase) for x in range(8))
                    )

                    order_db.insert_one(
                        {
                            "customer": ctx.author.name,
                            "customerid": ctx.author.id,
                            "order_id": order_id,
                            "order_status": "SUCCESS",
                        }
                    )

                    e = nextcord.Embed(
                        title=f"Order For {item} | Order ID: `{order_id}`",
                        description="If the bot doesnt respond to you it is a common bug that we cant fix so please be patient and try again around 15-20 mins.",
                        color=nextcord.Color.blue(),
                    )
                    e.set_image(url=images_results["thumbnail"])
                    e.set_footer(text=f"Source: {images_results['source']}")
                    await ctx.send(embed=e)
                    await asyncio.sleep(10)
                    delete_order = db.find_one({"customerid": ctx.author.id})
                    if delete_order:
                        order_db.find_one_and_delete({"customerid": ctx.author.id})
                    else:
                        return
                else:
                    e = nextcord.Embed(
                        title="Oops that seems like a non alcoholic drink!",
                        description="In the new Virtual Beer version, We decided to only whitelist alcoholic beverages. Find drinks here: [Click Me](https://www.thecocktaildb.com)",
                        color=nextcord.Color.blue(),
                    )
                    return await ctx.send(embed=e)
            else:
                return await ctx.reply("You dont have enough money!")

    @commands.command()
    async def refund(self, ctx, *, orderid=None):
        if orderid == None:
            await ctx.send("You need to specify the order id!")
        else:
            get_status = order_db.find_one({"order_id": orderid})
            if get_status:
                find_balance = db.find_one({"userid": ctx.author.id})
                await ctx.send(f"Please wait, Refunding your order of id: `{orderid}`")
                order_db.delete_one({"customerid": ctx.author.id})
                db.update_one(
                    {"userid": ctx.author.id},
                    {"$set": {"money": 50 + find_balance["money"]}},
                )
                await ctx.send("Your order has been refunded!")
            else:
                await ctx.send(
                    f"Your order with ID `{orderid}` is not found, Or not refundable anymore."
                )

    @commands.command()
    async def drink(self, ctx, *, name: str = None):
        if name == None:
            return await ctx.send("You need to mention a drink name.")
        else:
            x = get_drink_data(name)
            if x == True:
                data = DrinkInfo(name)
                e = nextcord.Embed(
                    title=name.title(),
                    description=data.instructions(),
                    color=nextcord.Color.blue(),
                )
                e.set_thumbnail(url=data.thumb())
                await ctx.send(embed=e)
            else:
                e = nextcord.Embed(
                    title="Oops that seems like a non alcoholic drink!",
                    description="In the new Virtual Beer version, We decided to only whitelist alcoholic beverages. Find drinks here: [Click Me](https://www.thecocktaildb.com)",
                    color=nextcord.Color.blue(),
                )
                return await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Order(bot))
