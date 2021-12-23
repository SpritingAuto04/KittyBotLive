import http.client
import mimetypes
import json
import discord
import random
import datetime
from discord.ext import commands
from config import random_color

aliases = ['Lick', 'LICK']
description = "This command uses Wynter's API, made by Darkmane Arweinydd#0069, to lick people!"


class Wholesome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases,
                      description=description)
    async def lick(self, message, *, licked: discord.Member = None):

        conn = http.bot.HTTPSConnection("api.furrycentr.al")
        payload = ''
        headers = {
            'Cookie': '__cfduid=d9a224e3d8c1cb5402581c2ae57ae3ec21605192790'
        }
        conn.request("GET", "/sfw/lick/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        data = json.loads(data)
        url = data["result"]["imgUrl"]
        color = random.choice(random_color)
        guild = message.guild
        msg = message
        _ment_lick = licked.display_name
        auth = msg.author.display_name
        lick = [f"***{auth}** licked **{_ment_lick}***",
                f"***{auth}** just randomly licks **{_ment_lick}** for no apparent reason*",
                f"***{_ment_lick}** asks **{auth}** to lick them so **{auth}** happily obliged*"]
        lickmessage = random.choice(lick)

        e_url = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())
        e_url.add_field(name=lickmessage, value=f":frame_photo: [Link to image]({url})", inline=False)
        e_url.set_image(url=url)
        e_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        if auth == _ment_lick:
            return await msg.channel.send(
                f"You can't really lick yourself, {auth}, so I will lick you! *gives plenty of licks*")

        else:
            return await msg.channel.send(embed=e_url)


def setup(bot):
    bot.add_cog(Wholesome(bot))
