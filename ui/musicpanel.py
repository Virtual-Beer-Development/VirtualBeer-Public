import nextcord
import wavelink
import json
from nextcord.ext import commands

with open("config/emojies.json") as f:
    data = json.load(f)
    status_code_ok = data["OK"]
    status_code_err = data["ERROR"]


class PanelUI(nextcord.ui.View):
    author: nextcord.User
    player: wavelink.Player = None

    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(emoji="⏩", style=nextcord.ButtonStyle.grey, custom_id="resume")
    async def resume(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        vc: wavelink.Player = self.player

        if not vc.is_playing():
            return await interaction.response.send_message(
                f"{status_code_err} | Im not playing anything!", ephemeral=True
            )
        if not vc.is_connected():
            return await interaction.response.send_message(
                f"{status_code_err} | Your not in a voice channel!", ephemeral=True
            )
        if not vc.is_paused():
            return await interaction.response.send_message(
                f"{status_code_err} | The track is not paused!", ephemeral=True
            )
        if interaction.user.id != self.author.id:
            print("Author is not in the bot voice channel")
            return await interaction.response.send_message(
                f"{status_code_err} | You are not the owner of this panel!",
                ephemeral=True,
            )
        if vc.is_paused():
            await vc.resume()
            return await interaction.response.send_message(
                f"{status_code_ok} | Resumed the player!", ephemeral=True
            )

    @nextcord.ui.button(emoji="⏸", style=nextcord.ButtonStyle.grey, custom_id="pause")
    async def pause(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        vc: wavelink.Player = self.player

        if not vc.is_playing():
            return await interaction.response.send_message(
                f"{status_code_err} | Im not playing anything!", ephemeral=True
            )
        if not vc.is_connected():
            return await interaction.response.send_message(
                f"{status_code_err} | Your not in a voice channel!", ephemeral=True
            )
        if vc.is_paused():
            return await interaction.response.send_message(
                f"{status_code_err} | The track is already paused!", ephemeral=True
            )
        if interaction.user.id != self.author.id:
            print("Author is not in the bot voice channel")
            return await interaction.response.send_message(
                f"{status_code_err} | You are not the owner of this panel!",
                ephemeral=True,
            )
        if not vc.is_paused():
            await vc.pause()
            return await interaction.response.send_message(
                f"{status_code_ok} | Paused the player!", ephemeral=True
            )

    @nextcord.ui.button(emoji="⏭", style=nextcord.ButtonStyle.grey, custom_id="skip")
    async def skip(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        vc: wavelink.Player = self.player

        if not vc.is_playing():
            return await interaction.response.send_message(
                f"{status_code_err} | Im not playing anything!", ephemeral=True
            )
        if not vc.is_connected():
            return await interaction.response.send_message(
                f"{status_code_err} | Your not in a voice channel!", ephemeral=True
            )
        if interaction.user.id != self.author.id:
            print("Author is not in the bot voice channel")
            return await interaction.response.send_message(
                f"{status_code_err} | You are not the owner of this panel!",
                ephemeral=True,
            )
        else:
            await vc.resume()
            return await interaction.response.send_message(
                f"{status_code_ok} | Skipped the player!", ephemeral=True
            )

    @nextcord.ui.button(emoji="⏹", style=nextcord.ButtonStyle.grey, custom_id="stop")
    async def stop(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        vc: wavelink.Player = self.player

        if not vc.is_playing():
            return await interaction.response.send_message(
                f"{status_code_err} | Im not playing anything!", ephemeral=True
            )
        if not vc.is_connected():
            return await interaction.response.send_message(
                f"{status_code_err} | Your not in a voice channel!", ephemeral=True
            )
        if interaction.user.id != self.author.id:
            print("Author is not in the bot voice channel")
            return await interaction.response.send_message(
                f"{status_code_err} | You are not the owner of this panel!",
                ephemeral=True,
            )
        else:
            await vc.stop()
            return await interaction.response.send_message(
                f"{status_code_ok} | Stopped the player!", ephemeral=True
            )

    @nextcord.ui.button(emoji="🔁", style=nextcord.ButtonStyle.blurple, custom_id="loop")
    async def loop(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        vc: wavelink.Player = self.player

        if not vc.is_playing():
            return await interaction.response.send_message(
                f"{status_code_err} | Im not playing anything!", ephemeral=True
            )
        if not vc.is_connected():
            return await interaction.response.send_message(
                f"{status_code_err} | Your not in a voice channel!", ephemeral=True
            )
        if interaction.user.id != self.author.id:
            print("Author is not in the bot voice channel")
            return await interaction.response.send_message(
                f"{status_code_err} | You are not the owner of this panel!",
                ephemeral=True,
            )
        else:
            try:
                vc.loop ^= True
            except Exception:
                setattr(vc, "loop", False)

            if vc.loop:
                return await interaction.response.send_message(
                    f"{status_code_ok} | Disbaled Loop for the track!", ephemeral=True
                )
            else:
                return await interaction.response.send_message(
                    f"{status_code_ok} | Enabled Loop for the track!", ephemeral=True
                )

    @nextcord.ui.button(
        emoji="🛑", style=nextcord.ButtonStyle.red, custom_id="disconnect"
    )
    async def leave(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        vc: wavelink.Player = self.player

        if not vc.is_playing():
            return await interaction.response.send_message(
                f"{status_code_err} | Im not playing anything!", ephemeral=True
            )
        if not vc.is_connected():
            return await interaction.response.send_message(
                f"{status_code_err} | Your not in a voice channel!", ephemeral=True
            )
        if interaction.user.id != self.author.id:
            print("Author is not in the bot voice channel")
            return await interaction.response.send_message(
                f"{status_code_err} | You are not the owner of this panel!",
                ephemeral=True,
            )
        else:
            await vc.disconnect()
            return await interaction.response.send_message(
                f"{status_code_ok} | Left the voice channel!"
            )
