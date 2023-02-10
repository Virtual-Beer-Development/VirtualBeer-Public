import os
import json
from utils.client import BarClient

bot = BarClient()

for files in os.listdir('./src/app_commands/devs'):
    if files.endswith('.py'):
        bot.load_extension(f'src.app_commands.devs.{files[:-3]}')
        print(f'Loaded {files[:-3]}')

for files in os.listdir('./src/app_commands/economy'):
    if files.endswith('.py'):
        bot.load_extension(f'src.app_commands.economy.{files[:-3]}')
        print(f'Loaded {files[:-3]}')

for files in os.listdir('./src/app_commands/fun'):
    if files.endswith('.py'):
        bot.load_extension(f'src.app_commands.fun.{files[:-3]}')
        print(f'Loaded {files[:-3]}')

for files in os.listdir('./src/devs'):
    if files.endswith('.py'):
        bot.load_extension(f'src.devs.{files[:-3]}')
        print(f'Loaded {files[:-3]}')

for files in os.listdir('./src/economy'):
    if files.endswith('.py'):
        bot.load_extension(f'src.economy.{files[:-3]}')
        print(f'Loaded {files[:-3]}')

for files in os.listdir('./src/events'):
    if files.endswith('.py'):
        bot.load_extension(f'src.events.{files[:-3]}')
        print(f'Loaded {files[:-3]}')

for files in os.listdir('./src/fun'):
    if files.endswith('.py'):
        bot.load_extension(f'src.fun.{files[:-3]}')
        print(f'Loaded {files[:-3]}')

for files in os.listdir('./src/misc'):
    if files.endswith('.py'):
        bot.load_extension(f'src.misc.{files[:-3]}')
        print(f'Loaded {files[:-3]}')

for files in os.listdir('./src/moderation'):
    if files.endswith('.py'):
        bot.load_extension(f'src.moderation.{files[:-3]}')
        print(f'Loaded {files[:-3]}')

for files in os.listdir('./src/music'):
    if files.endswith('.py'):
        bot.load_extension(f'src.music.{files[:-3]}')
        print(f'Loaded {files[:-3]}')

for files in os.listdir('./src/order'):
    if files.endswith('.py'):
        bot.load_extension(f'src.order.{files[:-3]}')
        print(f'Loaded {files[:-3]}')

with open("config/config.json") as f:
    conf = json.load(f)

try:
    bot.run(conf["TOKEN"])
except Exception as e:
    print(f"Bot has failed to start. Error: {e}")

