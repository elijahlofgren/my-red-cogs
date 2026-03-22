from .memberparty import MemberParty

async def setup(bot):
    await bot.add_cog(MemberParty(bot))