from .coc import Coc


async def setup(bot):
    cog = Coc(bot)
    await cog.initialize()
    bot.add_cog(cog)
