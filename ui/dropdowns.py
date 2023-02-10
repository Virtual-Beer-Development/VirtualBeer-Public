import nextcord
from nextcord.ext import commands


class HelpDropDown(nextcord.ui.Select):
    def __init__(self, user):
        self.user = user

        options = [
            nextcord.SelectOption(
                label="Economy", description="It's all about money", emoji="💸"
            ),
            nextcord.SelectOption(
                label="Fun", description="It's fun or nothing", emoji="🌝"
            ),
            nextcord.SelectOption(
                label="Moderation",
                description="Tones the rowdyness of a bar fairly down.",
                emoji="🔨",
            ),
            nextcord.SelectOption(
                label="Music",
                description="Every good bar has some good music.",
                emoji="🎛️",
            ),
            nextcord.SelectOption(
                label="Order",
                description="At the end, what's a bar without... drinks and food?",
                emoji="🍻",
            ),
            nextcord.SelectOption(
                label="Information",
                description="Some information about the bot.",
                emoji="ℹ",
            ),
        ]
        super().__init__(
            placeholder="What help do ya need?",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: nextcord.Interaction):
        if not int(self.user) == int(interaction.user.id):
            await interaction.response.send_message(
                "This is not your prompt!", ephemeral=True
            )

        if self.values[0] == "Economy":
            e = nextcord.Embed(
                title="💸 Economy Commands",
                description="""
                            `vb!balance [user]` - Check a user's balance.
                            `vb!work` - Get some money.
                            `vb!deposit` - Deposit money into your bank.
                            `vb!withdraw` - Withdraw money from your bank.
                            `vb!give` - Feeling generous? give someone money.
                            """,
                color=nextcord.Color.blue(),
            )
            await interaction.response.edit_message(embed=e)
        if self.values[0] == "Fun":
            e = nextcord.Embed(
                title="🌝 Fun Commands",
                description="""
                            `vb!pat` - Pat someone.
                            `vb!hug` - Give someone a big old hug.
                            `vb!slap` - Slap the heck out of someone.
                            `vb!kiss` - Give someone special a kiss.
                            `vb!cry` - Stop crying there is nothing to cry about.
                            `vb!bully` - Stop bullying people no one likes you.
                            `vb!poke` - Boop someone on their nose.
                            `vb!cuddle` - Cuddle with someone.
                            `vb!8ball` - Get a random response from the great 8ball.
                            `vb!coin` - Heads or Tails? Who knows.
                            `vb!img` - Get a random image from an AI, I would advise not to search up a person.
                            """,
                color=nextcord.Color.blue(),
            )
            await interaction.response.edit_message(embed=e)
        if self.values[0] == "Moderation":
            e = nextcord.Embed(
                title="🔨 Moderation Commands",
                description="""
                            `vb!ban [user] [reason]` - Bans a user from using the bot.
                            `vb!unban [user] [reason]` - Remove a user's ban.
                            `vb!resetacc [user] [reason]` - Reset's a users account balance and bank.
                            """,
                color=nextcord.Color.blue(),
            )
            await interaction.response.edit_message(embed=e)
        if self.values[0] == "Music":
            e = nextcord.Embed(
                title="🎵 Music Commands",
                description="""
                            `vb!play` - Plays a song from the given query.
                            `vb!skip` - Skip a currently playing song.
                            `vb!stop` - Stops a current song and clears the queue.
                            `vb!pause` - Pause a current song.
                            `vb!resume` - Resume a current song.
                            `vb!queue` - Gets the current queue.
                            `vb!volume` - Sets the volume form 1-100.
                            `vb!np` - Gets info on the current song playing.
                            `vb!loop` - Loops the current song.
                            `vb!disconnect` - Disconnect from a current voice channel.
                            """,
                color=nextcord.Color.blue(),
            )
            await interaction.response.edit_message(embed=e)
        if self.values[0] == "Order":
            e = nextcord.Embed(
                title="🍻 Food And Drinks Commands",
                description="""
                            `vb!order [order]` - Orders a drink.
                            `vb!drink [name]` - Gets info of a drink, If its available for you to order.
                            `vb!refund [orderid]` - Refund a drink.
                            """,
                color=nextcord.Color.blue(),
            )
            await interaction.response.edit_message(embed=e)
        if self.values[0] == "Information":
            e = nextcord.Embed(
                title="ℹ Information Commands",
                description="""
                            `vb!invite` - Gets the links of all platforms Virtual Beer is on.
                            `vb!rules` - Gets the rules of ordering foods and drinks.
                            `vb!banned` - Gets information on a banned user.
                            """,
                color=nextcord.Color.blue(),
            )
            return await interaction.response.edit_message(embed=e)


class HelpDropdownView(nextcord.ui.View):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.add_item(HelpDropDown(self.user))
