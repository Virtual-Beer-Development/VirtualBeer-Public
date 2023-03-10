import nextcord
import wavelink
import json
import datetime
from ui import musicpanel
from nextcord.ext import commands

with open("config/emojies.json") as f:
    data = json.load(f)
    status_code_ok = data["OK"]
    status_code_err = data["ERROR"]
    emoji_cd_playing = data["MUSIC_CD"]


class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["p"])
    async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(
                cls=wavelink.Player
            )
            await ctx.send(f"Connected to {ctx.author.voice.channel.name}!")
        elif not ctx.author.voice:
            return await ctx.send(
                f"{status_code_err} | Please join a voice channel before running this command."
            )
        elif ctx.author.voice.channel != ctx.me.voice.channel:
            return await ctx.send(
                f"{status_code_err} | I must be inside of the same voice channel as you!"
            )
        else:
            vc: wavelink.Player = ctx.voice_client

        if vc.queue.is_empty and not vc.is_playing():
            await vc.play(search)
            e = nextcord.Embed(
                title=f"Currently Playing | {search.title} ",
                color=nextcord.Color.random(),
            )
            e.add_field(
                name="Duration",
                value=f"`{str(datetime.timedelta(seconds=vc.track.duration))}`",
            )
            e.add_field(name="Song URL", value=f"[Click Me]({str(vc.track.uri)})")
            e.set_thumbnail(url=search.thumbnail)
            view = musicpanel.PanelUI()
            view.player = vc
            view.author = ctx.author
            await ctx.send(embed=e, view=view)
            await view.wait()
        else:
            await vc.queue.put_wait(search)
            e = nextcord.Embed(
                title=f"{search.title} | Added to the queue",
                color=nextcord.Color.random(),
            )
            e.add_field(
                name="Duration",
                value=f"`{str(datetime.timedelta(seconds=vc.track.duration))}`",
            )
            e.add_field(name="Song URL", value=f"[Click Me]({str(vc.track.uri)})")
            e.set_thumbnail(url=search.thumbnail)
            await ctx.send(embed=e)
        vc.ctx = ctx
        setattr(vc, "loop", False)


def setup(bot):
    bot.add_cog(Play(bot))
