import nextcord
import textwrap
import os
import json
import sys
import datetime
from utils.client import BarClient
from nextcord.ext import commands
from nextcord import Color, Embed, TextInputStyle
from nextcord.ui import TextInput


class EvalModal(nextcord.ui.Modal):
    def __init__(self, bot: BarClient, chan_inter: nextcord.Interaction):
        self.bot = bot
        self.chan_inter = chan_inter
        super().__init__(title="Evaluate Modal")

        self.description = TextInput(label="Code Execution",
                                     placeholder="Enter code here...",
                                     max_length=2000,
                                     style=TextInputStyle.paragraph,
                                     required=True, custom_id="eval:code"
                                     )
        self.add_item(self.description)

    async def callback(self, inter: nextcord.Interaction):
        try:
            code = self.description.value
            env = {
                "bot": self.bot,
                "inter": self.chan_inter,
                "guild": self.chan_inter.guild,
                "author": self.chan_inter.user,
                "channel": self.chan_inter.channel,
                "nextcord": nextcord,
                "os": os,
                "sys": sys,
                "commands": commands,
                "self": self
            }
            env.update(globals())
            exec(f"async def func():\n{textwrap.indent(code, ' ')}", env)
            response = await eval("func()", env)

            if len(str(response)) > 1023:
                response = response[:1021] + "..."

            eval_embed = Embed(color=Color.green(), timestamp=datetime.datetime.now())
            eval_embed.add_field(name="Code", value=f"```py\n{code}\n```", inline=False)
            eval_embed.add_field(name="Response", value=f"```py\n{response}\n```", inline=False)
            eval_embed.set_author(name=inter.user, icon_url=inter.user.display_avatar.url)
            eval_embed.set_footer(text="Type: {type}".format(type=type(response).__name__))
            await inter.send(embed=eval_embed)
        except Exception as e:
            eval_err_embed = Embed(color=Color.green(), timestamp=datetime.datetime.now())
            eval_err_embed.add_field(name="Code", value=f"```py\n{code}\n```", inline=False)
            eval_err_embed.add_field(name="Error", value=f"```py\n{e.__class__.__name__}: {e}\n```", inline=False)
            eval_err_embed.set_author(name=inter.user, icon_url=inter.user.display_avatar.url)
            await inter.send(embed=eval_err_embed)
            return


class SlashDevs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Code execution via bot.")
    async def eval(self, interaction: nextcord.Interaction):
        with open("./config/config.json") as f:
            data = json.load(f)
            owner = data["OWNERSHIP"][0]["OWNER"]
            dev = data["OWNERSHIP"][0]["DEVELOPERS"]
        if interaction.user.id == owner:
            modal = EvalModal(self.bot, interaction)
            await interaction.response.send_modal(modal)
        elif interaction.user.id in dev:
            modal = EvalModal(self.bot, interaction)
            await interaction.response.send_modal(modal)
        else:
            await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)

    @nextcord.slash_command()
    async def reload(self, interaction: nextcord.Interaction):
        with open("./config/config.json") as f:
            data = json.load(f)
            owner = data["OWNERSHIP"][0]["OWNER"]
            dev = data["OWNERSHIP"][0]["DEVELOPERS"]

        if interaction.user.id == owner:
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

            return await interaction.response.send_message("Reloaded all cogs.")
        if interaction.user.id == dev:
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

            return await interaction.response.send_message("Reloaded all cogs.")
        else:
            return


def setup(bot):
    bot.add_cog(SlashDevs(bot))
