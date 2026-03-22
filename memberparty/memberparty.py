import discord
import random
from redbot.core import commands

class MemberParty(commands.Cog):
    """Announce when someone gets the Member role with vetted artsy & movie quotes."""

    def __init__(self, bot):
        self.bot = bot
        self.welcomes = [
            "Welcome {user}! 'I think this is the beginning of a beautiful friendship.' (Casablanca) 🥂",
            "Welcome {user}! 'Creativity takes courage.' (Henri Matisse) 🖌️",
            "Welcome {user}! 'To infinity and beyond!' (Toy Story) 🚀",
            "Welcome {user}! 'Every child is an artist.' (Picasso) 🎨",
            "Welcome {user}! 'Life moves pretty fast. If you don't stop and look around, you could miss it.' (Ferris Bueller) 🕶️",
            "Welcome {user}! 'May the Force be with you.' (Star Wars) ⚔️",
            "Welcome {user}! 'Art is not what you see, but what you make others see.' (Degas) 📸",
            "Welcome {user}! 'Adventure is out there!' (Up) 🎈",
            "Welcome {user}! 'Just keep swimming!' (Finding Nemo) 🐟",
            "Welcome {user}! 'Be excellent to each other, and party on!' (Bill & Ted) 🎸",
            "Welcome {user}! 'No matter what people tell you, words and ideas can change the world.' (Robin Williams) 💡",
            "Welcome {user}! 'Every artist dips his brush in his own soul.' (Beecher) 🌈",
            "Welcome {user}! 'Life is a great big canvas, throw all the paint you can on it.' (Danny Kaye) 🖼️",
            "Welcome {user}! 'The world is but a canvas to our imagination.' (Thoreau) 🎭",
            "Welcome {user}! 'I found that I could say things with color and shapes that I couldn't say any other way.' (O'Keeffe) 🎨",
            "Welcome {user}! 'The best way to predict the future is to create it.' (Peter Drucker) ✨",
            "Welcome {user}! 'The painting has a life of its own.' (Jackson Pollock) 🖌️",
            "Welcome {user}! 'Imagination is the beginning of creation.' (George Bernard Shaw) 🌟",
            "Welcome {user}! 'Go make good art.' (Neil Gaiman) ✍️",
            "Welcome {user}! 'The object of art is not to reproduce reality, but to create a reality of the same intensity.' (Giacometti) 🏛️"
        ]

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        # Configuration
        ROLE_NAME = "Member"
        CHANNEL_NAME = "general"
        WAVE_EMOJI = "👋"

        # Check for role gain
        had_role = discord.utils.get(before.roles, name=ROLE_NAME)
        has_role = discord.utils.get(after.roles, name=ROLE_NAME)

        if not had_role and has_role:
            channel = discord.utils.get(after.guild.text_channels, name=CHANNEL_NAME)
            
            if channel:
                # Select a random quote and format with the user mention
                welcome_phrase = random.choice(self.welcomes).format(user=after.mention)
                message = await channel.send(welcome_phrase)
                
                # Add the wave reaction for the community to click
                try:
                    await message.add_reaction(WAVE_EMOJI)
                except discord.HTTPException:
                    pass

async def setup(bot):
    await bot.add_cog(MemberParty(bot))