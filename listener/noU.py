import random

from discord.ext import commands


class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name="NoU")
    async def on_message(self, message):
        if not message.author.bot:
            if message.content.startswith("no u"):

                NeonnoUemoji = self.bot.get_emoji(916295744665833522)
                AnimatenoUemoji = self.bot.get_emoji(916295814547144704)

                reply = [
                    f"No you!",
                    f"{NeonnoUemoji}",
                    f"{AnimatenoUemoji}"
                ]

                await message.channel.reply(random.choice(reply))

            else:
                return


def setup(bot):
    bot.add_cog(Listeners(bot))
