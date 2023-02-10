import nextcord
from nextcord.ext import commands
import os
import json


class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reload(self, ctx):
        with open("./config/config.json") as f:
            data = json.load(f)
            owner = data["OWNERSHIP"][0]["OWNER"]
            dev = data["OWNERSHIP"][0]["DEVELOPERS"]

        if ctx.author.id == owner:
            print(owner)
            for files in os.listdir("./src/order"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.order.{files[:-3]}")
            print("Reloaded [ORDERS]")

            for files in os.listdir("./src/economy"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.economy.{files[:-3]}")
            print("Reloaded [ECONOMY]")

            for files in os.listdir("./src/fun"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.fun.{files[:-3]}")
            print("Reloaded [FUN]")

            for files in os.listdir("./src/misc"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.misc.{files[:-3]}")
            print("Reloaded [MISC]")

            for files in os.listdir("./src/moderation"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.moderation.{files[:-3]}")
            print("Reloaded [MODERATION]")

            for files in os.listdir("./src/music"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.music.{files[:-3]}")
            print("Reloaded [MUSIC]")

            for events in os.listdir("./src/events"):
                if events.endswith(".py"):
                    self.bot.reload_extension(f"src.events.{events[:-3]}")
            print("Reloaded [EVENTS]")

            for events in os.listdir("./src/app_commands/economy"):
                if events.endswith(".py"):
                    self.bot.reload_extension(f"src.app_commands.economy.{events[:-3]}")
            print("Loaded [SLASH-ECONOMY]")

            for devs in os.listdir("./src/devs"):
                if devs.endswith(".py"):
                    self.bot.reload_extension(f"src.devs.{devs[:-3]}")
                print("Loaded [DEVS]")

            return await ctx.send("Reloaded all cogs.")
        if ctx.author.id == dev:
            print(dev)
            for files in os.listdir("./src/order"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.order.{files[:-3]}")
            print("Reloaded [ORDERS]")

            for files in os.listdir("./src/economy"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.economy.{files[:-3]}")
            print("Reloaded [ECONOMY]")

            for files in os.listdir("./src/fun"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.fun.{files[:-3]}")
            print("Reloaded [FUN]")

            for files in os.listdir("./src/misc"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.misc.{files[:-3]}")
            print("Reloaded [MISC]")

            for files in os.listdir("./src/moderation"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.moderation.{files[:-3]}")
            print("Reloaded [MODERATION]")

            for files in os.listdir("./src/music"):
                if files.endswith(".py"):
                    self.bot.reload_extension(f"src.music.{files[:-3]}")
            print("Reloaded [MUSIC]")

            for events in os.listdir("./src/events"):
                if events.endswith(".py"):
                    self.bot.reload_extension(f"src.events.{events[:-3]}")
            print("Reloaded [EVENTS]")

            for events in os.listdir("./src/app_commands/economy"):
                if events.endswith(".py"):
                    self.bot.reload_extension(f"src.app_commands.economy.{events[:-3]}")
            print("Loaded [SLASH-ECONOMY]")

            for devs in os.listdir("./src/devs"):
                if devs.endswith(".py"):
                    self.bot.reload_extension(f"src.devs.{devs[:-3]}")
                print("Loaded [DEVS]")

            return await ctx.send("Reloaded all cogs.")
        else:
            return


def setup(bot):
    bot.add_cog(Reload(bot))
