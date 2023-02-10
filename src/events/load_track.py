import nextcord
import json
import wavelink
import datetime
import asyncio
from nextcord.ext import commands


class TrackEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_wavelink_track_end(
        self, player: wavelink.Player, track: wavelink.Track, reason
    ):
        ctx = player.ctx
        vc: wavelink.Player = ctx.voice_client

        if True:
            if vc.loop:
                return await vc.play(track)

            if vc.queue:
                next_song = vc.queue.get()
                await vc.play(next_song)
                get_thumbnail = wavelink.YouTubeTrack(vc.track.id, next_song.info)
                e = nextcord.Embed(
                    description=f"**Now Playing | [{next_song}]({str(vc.track.uri)})**",
                    color=nextcord.Color.random(),
                )
                e.add_field(
                    name="Duration",
                    value=f"`{str(datetime.timedelta(seconds=vc.track.duration))}`",
                )
                e.add_field(name="Song URL", value=f"[Click Me]({str(vc.track.uri)})")
                e.set_thumbnail(url=get_thumbnail.thumb)
                await ctx.send(embed=e)
            else:
                try:
                    queue = vc.queue.get()
                except wavelink.errors.QueueEmpty as e:
                    await asyncio.sleep(10)
                    try:
                        get_queue = vc.queue.get()
                        if get_queue:
                            pass
                    except wavelink.errors.QueueEmpty as e:
                        await vc.disconnect()
                    leave_message = nextcord.Embed(
                        title="Left the voice channel!",
                        description="Thank you for using Virtual Beer! We hope you have very wonderful time while using our bot! We really love your support that you have givin to us by inviting our bot!",
                        color=nextcord.Color.random(),
                    )
                    return await ctx.send(embed=leave_message)
        else:
            return await vc.stop()


def setup(bot):
    bot.add_cog(TrackEvents(bot))
