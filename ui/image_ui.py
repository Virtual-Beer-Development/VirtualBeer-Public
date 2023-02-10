import nextcord
from nextcord.ext import commands
import base64
from io import BytesIO


class ImageDropdown(nextcord.ui.Select):
    def __init__(self, msg, images, user):
        self.msg = msg
        self.images = images
        self.user = user

        options = [
            nextcord.SelectOption(label="1"),
            nextcord.SelectOption(label="2"),
            nextcord.SelectOption(label="3"),
            nextcord.SelectOption(label="4"),
            nextcord.SelectOption(label="5"),
            nextcord.SelectOption(label="6"),
            nextcord.SelectOption(label="7"),
            nextcord.SelectOption(label="8"),
            nextcord.SelectOption(label="9"),
        ]

        super().__init__(
            placeholder="Choose an image!",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: nextcord.Interaction):
        if not int(self.user) == int(interaction.user.id):
            await interaction.response.send_message(
                "This is not your prompt!", ephemeral=True
            )
        selection = int(self.values[0]) - 1
        image = BytesIO(base64.decodebytes(self.images[selection].encode("utf-8")))
        return await self.msg.edit(
            content="These are the generated images!",
            file=nextcord.File(image, "generatedImage.png"),
            view=ImageDropdownView(self.msg, self.images, self.user),
        )


class ImageDropdownView(nextcord.ui.View):
    def __init__(self, msg, images, user):
        super().__init__()
        self.msg = msg
        self.images = images
        self.user = user
        self.add_item(ImageDropdown(self.msg, self.images, self.user))
