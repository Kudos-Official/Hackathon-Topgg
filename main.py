import discord
from discord.ext import commands
import discord_ui
from discord_ui import UI
prefix="s?"
example=discord.Activity(type=discord.ActivityType.watching, name=f"{prefix}help ❄️☃️")
bot=commands.Bot(command_prefix=["s?","S?"], case_insensitive=True, intents=discord.Intents.all(),allowed_mentions=discord.AllowedMentions(roles=True, users=True, everyone=False),activity=example)
initial_extensions=['cogs.ProhibitedWord Related', 'cogs.ChristmasEconomy Related', 'cogs.Mod Related', 'cogs.Utility And Fun Related']
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
class MyHelp(commands.HelpCommand):
    #BOT HELP
    async def send_bot_help(self, mapping):
        channel=self.get_destination()
        author=self.context.author
        emoji=bot.get_emoji(878552435575111690)
        py=bot.get_emoji(878552448149631016)
        edit=bot.get_emoji(895264989508669480)
        right=bot.get_emoji(893361416826929193)
        owner=bot.get_user(760504975075180564)
        circle=bot.get_emoji(895314994772713472)
        includes=bot.get_emoji(878552446979440671)
        commandsemoji=bot.get_emoji(893359685632143400)
        embed=discord.Embed(color=0x009EFF, title=f'{emoji} Help {emoji}')
        embed.set_author(name=author, icon_url=author.avatar_url)
        for i in bot.cogs:
          cog=bot.get_cog(i)
          commands=cog.get_commands()
          listtosend=""
          howmanycommands=0
          for j in commands:
            if listtosend=="":
              listtosend=f'`{j.name}`'
              howmanycommands=howmanycommands+1
            else:
              listtosend=f'{listtosend}, `{j.name}`'
              howmanycommands=howmanycommands+1
          embed.add_field(name=f'{circle} {cog.qualified_name} [`{howmanycommands}`]', value=f'> {commandsemoji} **Description:**\n{cog.description}\n> {includes} **Includes:**\n{listtosend}')
        prime=bot.get_user(816235165801513002)
        embed.add_field(name=f"{py} Credits {py}",value=f"This bot is made using {edit} [**discord.py**](https://discordpy.readthedocs.io/en/stable/) {edit}\nSpecial thanks to all people who helped me in the {edit} [**discord.py discord server**](https://discord.gg/dpy) {edit}\nThanks for creating the discord.py library, {edit} [**Danny#0007**](https://discord.com/users/80088516616269824) {edit}\n\n{right} This bot is not affiliated with any of the discord.py users except the bot owners [**{owner.display_name}#{owner.discriminator}**](https://discord.com/users/760504975075180564), [**{prime.display_name}#{prime.discriminator}**](https://discord.com/users/816235165801513002)", inline=False)
        embed.set_footer(text="Thanks for using me!", icon_url=bot.user.avatar_url)
        await channel.send(embed=embed)
    #COMMAND HELP
    async def send_command_help(self, command):
        channel=self.get_destination()
        author=self.context.author
        emoji=bot.get_emoji(878552435575111690)
        py=bot.get_emoji(878552448149631016)
        edit=bot.get_emoji(895264989508669480)
        right=bot.get_emoji(893361416826929193)
        owner=bot.get_user(760504975075180564)
        circle=bot.get_emoji(895314994772713472)
        commandsemoji=bot.get_emoji(893359685632143400)
        cmd=command
        embed=discord.Embed(color=0x009EFF, title=f'{emoji} Help {emoji}', description=f'**{author.name}**, here is help on `{cmd.name}`')
        embed.add_field(name=f'{circle} Command {cmd.name}\'s Description', value=f'{commandsemoji} `{cmd.description}`')
        embed.add_field(name=f'{circle} Command {cmd.name}\'s Syntax', value=f'{commandsemoji} `{cmd.help}`')
        embed.add_field(name=f'{circle} {cmd.name}\'s Aliases', value=f'{commandsemoji} `{"`, `".join(cmd.aliases)}`')
        embed.set_author(name=author, icon_url=author.avatar_url)
        prime=bot.get_user(816235165801513002)
        embed.add_field(name=f"{py} Credits {py}",value=f"This bot is made using {edit} [**discord.py**](https://discordpy.readthedocs.io/en/stable/) {edit}\nSpecial thanks to all people who helped me in the {edit} [**discord.py discord server**](https://discord.gg/dpy) {edit}\nThanks for creating the discord.py library, {edit} [**Danny#0007**](https://discord.com/users/80088516616269824) {edit}\n\n{right} This bot is not affiliated with any of the discord.py users except the bot owners [**{owner.display_name}#{owner.discriminator}**](https://discord.com/users/760504975075180564), [**{prime.display_name}#{prime.discriminator}**](https://discord.com/users/816235165801513002)", inline=False)
        embed.set_footer(text="Thanks for using me!", icon_url=bot.user.avatar_url)
        await channel.send(embed=embed)
    #COG HELP
    async def send_cog_help(self, cog):
        channel=self.get_destination()
        author=self.context.author
        emoji=bot.get_emoji(878552435575111690)
        py=bot.get_emoji(878552448149631016)
        edit=bot.get_emoji(895264989508669480)
        right=bot.get_emoji(893361416826929193)
        owner=bot.get_user(760504975075180564)
        circle=bot.get_emoji(895314994772713472)
        commandsemoji=bot.get_emoji(893359685632143400)
        embed=discord.Embed(color=0x009EFF, title=f'{emoji} Help {emoji}')
        embed.set_author(name=author, icon_url=author.avatar_url)
        listtosend=""
        howmanycommands=0
        for j in cog.get_commands():
          if listtosend=="":
              listtosend=f'`{j.name}`'
              howmanycommands=howmanycommands+1
          else:
              listtosend=f'{listtosend}, `{j.name}`'
              howmanycommands=howmanycommands+1
        embed.add_field(name=f'{circle} Category {cog.qualified_name}\'s description', value=f'{commandsemoji} `{cog.description}`')
        embed.add_field(name=f'{circle} Category {cog.qualified_name} includes [`{howmanycommands}`] commands', value=f'{commandsemoji} {listtosend}')
        prime=bot.get_user(816235165801513002)
        embed.add_field(name=f"{py} Credits {py}",value=f"This bot is made using {edit} [**discord.py**](https://discordpy.readthedocs.io/en/stable/) {edit}\nSpecial thanks to all people who helped me in the {edit} [**discord.py discord server**](https://discord.gg/dpy) {edit}\nThanks for creating the discord.py library, {edit} [**Danny#0007**](https://discord.com/users/80088516616269824) {edit}\n\n{right} This bot is not affiliated with any of the discord.py users except the bot owners [**{owner.display_name}#{owner.discriminator}**](https://discord.com/users/760504975075180564), [**{prime.display_name}#{prime.discriminator}**](https://discord.com/users/816235165801513002)", inline=False)
        embed.set_footer(text="Thanks for using me!", icon_url=bot.user.avatar_url)
        await channel.send(embed=embed)
bot.help_command=MyHelp()
ui=UI(bot)
bot.run("OTE4ODA2NDk0NzgxMjQ3NDg4.YbMnOg.YQ9KnMoSjNHZpfv0Euf6NsWrKlE")
