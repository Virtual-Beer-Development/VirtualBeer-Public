import nextcord
import random
import animec

from nextcord.ext import commands
from animec import Waifu


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="8ball", description="Ask the magic 8ball")
    async def eightball(self, interaction: nextcord.Interaction, *, question: str):
        if question is None:
            return await interaction.send("Whats your question dummy!")
        else:
            responses = [
                "No, Im not a wizard.",
                "Yea, Maybe sure...",
                "How about you give me a cookie.",
                "Oh yea ofc, No.",
                "Maybe yea.",
                "Im giving you 5 seconds to take that back.",
            ]
            res = random.choice(responses)

            e = nextcord.Embed(title="🎱 The Ball Has Spoken 🎱", description=res)
            await interaction.response.send_message(embed=e)

    @nextcord.slash_command(description="Flip the coin!")
    async def coinflip(self, interaction: nextcord.Interaction):
        chances = [0, 1]
        choice = random.choice(chances)

        if choice == 0:
            await interaction.response.send_message("The coin has landed on... **`Tails`** ✨")
        else:
            await interaction.response.send_message("The coin has landed on... **`Heads`** ✨")

    @nextcord.slash_command()
    async def bully(self, interaction: nextcord.Interaction, user: nextcord.User = None):
        if user == None:
            return await interaction.response.send_message("You cant bully yourself silly!")
        else:
            gif = Waifu.bully()
            e = nextcord.Embed(
                title=f"{interaction.user.name} Bully's {user.name}",
                description="Remember, Dont bully people kids!",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await interaction.response.send_message(embed=e)

    @nextcord.slash_command()
    async def cuddle(self, interaction: nextcord.Interaction, user: nextcord.User = None):
        if user == None:
            return await interaction.response.send_message("You cant cuddle yourself silly!")
        else:
            gif = Waifu.cuddle()
            e = nextcord.Embed(
                title=f"{interaction.user.name} Cuddles {user.name}!",
                description="Omg! So cute to see these two cuddle!",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await interaction.response.send_message(embed=e)

    @nextcord.slash_command()
    async def cry(self, interaction: nextcord.Interaction):
        gif = Waifu.cry()
        e = nextcord.Embed(
            title=f"{interaction.user.name} Is Crying!",
            description="Aww, Dont cry...",
            color=nextcord.Color.blue(),
        )
        e.set_image(url=gif)
        await interaction.response.send_message(embed=e)

    @nextcord.slash_command()
    async def hug(self, interaction: nextcord.Interaction, user: nextcord.User = None):
        if user == None:
            return await interaction.response.send_message("You cant hug yourself silly!")
        else:
            gif = Waifu.hug()
            e = nextcord.Embed(
                title=f"{interaction.user.name} Gave Hugs To {user.name}!",
                description="Give me a hug too! :C",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await interaction.response.send_message(embed=e)

    @nextcord.slash_command()
    async def pat(self, interaction: nextcord.Interaction, user: nextcord.User = None):
        if user == None:
            return await interaction.response.send_message("You cant pat yourself silly!")
        else:
            gif = Waifu.pat()
            e = nextcord.Embed(
                title=f"{interaction.user.name} Gave Pats To {user.name}!",
                description="How cute can that be!",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await interaction.response.send_message(embed=e)

    @nextcord.slash_command()
    async def slap(self, interaction: nextcord.Interaction, user: nextcord.User = None):
        if user == None:
            return await interaction.response.send_message("You cant slap yourself silly!")
        else:
            gif = Waifu.slap()
            e = nextcord.Embed(
                title=f"{interaction.user.name} Slapped {user.name}!",
                description="Ouch! That's gonna leave a mark...",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await interaction.response.send_message(embed=e)

    @nextcord.slash_command()
    async def kiss(self, interaction: nextcord.Interaction, user: nextcord.User = None):
        if user == None:
            return await interaction.response.send_message("You cant kiss yourself silly!")
        else:
            gif = Waifu.kiss()
            e = nextcord.Embed(
                title=f"{interaction.user.name} Kissed {user.name}!",
                description="Mazel Tov! 🙌",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await interaction.response.send_message(embed=e)

    @nextcord.slash_command()
    async def poke(self, interaction: nextcord.Interaction, user: nextcord.User = None):
        if user == None:
            return await interaction.response.send_message("You cant hug yourself silly!")
        else:
            gif = Waifu.poke()
            e = nextcord.Embed(
                title=f"{interaction.user.name} Poked {user.name}!",
                description="Boop Boop Boop!",
                color=nextcord.Color.blue(),
            )
            e.set_image(url=gif)
            await interaction.response.send_message(embed=e)


def setup(bot):
    bot.add_cog(Fun(bot))
