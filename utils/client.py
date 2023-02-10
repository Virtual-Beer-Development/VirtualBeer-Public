from nextcord import AllowedMentions, Activity, ActivityType, Intents, Status
from nextcord.ext import commands


class BarClient(commands.Bot):
    def __init__(self):
        super().__init__(activity=Activity(type=ActivityType.watching, name=f"The Bar!"),
                         command_prefix="avb!",
                         allowed_mentions=AllowedMentions(everyone=False, users=True, roles=False),
                         intents=Intents.all(),
                         status=Status.dnd,
                         help_command=None
                         )
