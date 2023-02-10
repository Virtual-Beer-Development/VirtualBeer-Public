import nextcord
from nextcord.ext import commands
import aiohttp
from io import BytesIO
import time
import base64
from ui.image_ui import ImageDropdownView


class Aimage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def img(self, ctx, *, prompt: str = None):
        if not prompt:
            wait_time = int(time.time() + 60)
            tip_msg = await ctx.send(
                "Did you know? You can get a random image from a search prompt! example: `vb!img coffee`"
            )
            send_img = await ctx.send(
                f"Getting image ready... Estimated Time: <t:{wait_time}:R>"
            )
            async with aiohttp.request(
                "POST", "https://backend.craiyon.com/generate", json={"prompt": "Beer"}
            ) as res:
                r = await res.json()
                images = r["images"]
            image = BytesIO(base64.decodebytes(images[0].encode("utf-8")))
            return await send_img.edit(
                content="These are the generated images!",
                file=nextcord.File(image, "generatedImage.png"),
                view=ImageDropdownView(send_img, images, ctx.author.id),
            )
        else:
            wait_time = int(time.time() + 60)
            send_img = await ctx.send(
                f"Getting image ready... Estimated Time: <t:{wait_time}:R>"
            )
            async with aiohttp.request(
                "POST", "https://backend.craiyon.com/generate", json={"prompt": prompt}
            ) as res:
                r = await res.json()
                images = r["images"]
            image = BytesIO(base64.decodebytes(images[0].encode("utf-8")))
            return await send_img.edit(
                content="These are the generated images!",
                file=nextcord.File(image, "generatedImage.png"),
                view=ImageDropdownView(send_img, images, ctx.author.id),
            )


def setup(bot):
    bot.add_cog(Aimage(bot))
