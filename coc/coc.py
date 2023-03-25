import discord
from redbot.core import commands, Config
#grdrdrtdrtdrdhrdtrhdhtrd
from re import sub

class Coc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=424242)
        default_user = {"tag": {}}
        self.config.register_user(**default_user)
        self.baseurl = "https://api.clashofclans.com/v1/"

    async def initialize(self):
        cockey = await self.bot.get_shared_api_tokens("cocapi")
        token = cockey["api_key"]
        if token is None:
            raise ValueError("CoC API key has not been set.")
        self.headers = {
            "authorization": f"Bearer {token}",
            "Accept": "application/json",
        }

    def apirequest(self, url: str):
        url = self.baseurl + url
        try:
            response = httpx.get(url=url, headers=self.headers, timeout=20)
            return response.json()
        except Exception as e:
            return e
       
    @commands.command()
    async def find_member(self, ctx, member: discord.Member):
        for u in self.config.all_users():
            if discord.utils.escape_markdown(u.display_name.lower()) == discord.utils.escape_markdown(member.display_name.lower()):
                await ctx.send(self.config.user(u).tag())
        await ctx.send("No matches were found.")
    
    @commands.command()
    async def get(self, ctx, tag: str):
        """Takes in the clan's tag and returns clan info"""

        tag = "clans/%23" + tag.replace("#", "")
        clan_json = self.apirequest(tag)
        
        try:
            if clan_json['clanLevel'] < 5:
                donation_upgrade = 0
            elif clan_json['clanLevel'] < 10:
                donation_upgrade = 1
            else:
                donation_upgrade = 2
        except:
            return await ctx.send(clan_json)
        
        await ctx.send("All went good.")
        #then you can just use clan_json['field'] to display info about the clan. docs are available, you can check them, I'm not a coc expert so idk what to put here

