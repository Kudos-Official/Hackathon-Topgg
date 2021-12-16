import discord
from discord.ext import commands
from replit import db
from discord_ui import Button
import asyncio
import datetime
import time
import json
def setvalue(loaded):
    with open("db.json", "w") as f:
        json.dump(loaded, f, indent=4)
def setvar(var, guild, value):
    with open("db.json", "r") as f:
        loaded=json.load(f)
    try:
        result=loaded[f"{var}_{str(guild.id)}"]
    except:
        loaded[f"{var}_{str(guild.id)}"]=value
        setvalue(loaded)
    else:
        pass
def openfile():
    with open("db.json", "r") as f:
        return json.load(f)
def notadmin(self):
    cross=self.bot.get_emoji(919263807732318249)
    notadmin=f"{cross} You require the `ADMINISTRATOR` permissions to be able to execute this command"
    return notadmin
def cross(self):
  return self.bot.get_emoji(920962093065318421)
def tick(self):
  return self.bot.get_emoji(920961667335065650)
def dot(self):
  return self.bot.get_emoji(920962310368002058)
class BlacklistedWords(commands.Cog):
    """Blacklisted Words Related Commands"""
    def __init__(self, bot):
      self.bot=bot
    @commands.command(aliases=['blacklistedwordadd'], description='Add A Word That Warns A User If They Use It', help="addbw <word>")
    @commands.has_permissions(administrator=True)
    async def addbw(self, ctx, *, word=None):
      loaded=openfile()
      try:
        loaded[f"badword_{str(ctx.guild.id)}"]
      except:
        setvar("badword", ctx.guild, [])
        setvar("whoadded", ctx.guild, [])
        setvar("timestamp", ctx.guild, [])
      else:
        pass
      if not word:
        await ctx.send(f"{cross(self)} Word not provided")
      else:
        if word.lower() in loaded[f"badword_{str(ctx.guild.id)}"]:
          await ctx.send(f"{cross(self)} Word already exists")
        else:
          embed=discord.Embed(title="Confirmation", description=f"{dot(self)} Do you wish to confirm the addition of the word `{word}` into the bad word list?", color=discord.Color.random())
          embed.set_footer(text="Click the appropriate button!", icon_url=ctx.author.avatar_url)
          messageid=await ctx.send(content=ctx.author.mention, embed=embed, components=[Button("Add The Word", color="green", emoji="✅"), Button("Cancel The Request", color="red", emoji="❌")])
          try:
            btn=await messageid.wait_for("button", self.bot, timeout=30)
            if btn.author!=ctx.author:
              await btn.respond(content=self.bot.notauthor, hidden=True)
            else:
              if btn.component.label.lower()=="add the word":
                await btn.respond(f"{tick(self)} Added `{word}` to the bad-word list")
                loaded[f"badword_{str(ctx.guild.id)}"].append(word.lower())
                loaded[f"whoadded_{str(ctx.guild.id)}"].append(ctx.author.id)
                loaded[f"timestamp_{str(ctx.guild.id)}"].append(f"<t:{int(time.time())}>")
                setvalue(loaded)
                embed=discord.Embed(title="Added", description=f"{tick(self)} The requested word `{word}` was added", color=0x00FF00)
                embed.set_footer(text="Now anyone saying the word in chat shall be warned", icon_url=ctx.author.avatar_url)
                await messageid.edit(content=ctx.author.mention, embed=embed, components=[Button("Add The Word", color="green", emoji="✅", disabled=True), Button("Cancel The Request", color="red", emoji="❌", disabled=True)])
              else:
                await btn.respond(f"{cross(self)} Alright, lets pretend that never happened..")
                embed=discord.Embed(title="Cancelled", description=f"{cross(self)} The requested word `{word}` was not added", color=0xFF0000)
                embed.set_footer(text="🤷", icon_url=ctx.author.avatar_url)
                await messageid.edit(content=ctx.author.mention, embed=embed, components=[Button("Add The Word", color="green", emoji="✅", disabled=True), Button("Cancel The Request", color="red", emoji="❌", disabled=True)])
          except asyncio.TimeoutError:
            embed=discord.Embed(title="Cancelled(Timeout)", description=f"{cross(self)} The requested word `{word}` was not added due to exceeding the 30 second timeout", color=0xFF0000)
            embed.set_footer(text="🤷", icon_url=ctx.author.avatar_url)
            await messageid.edit(content=ctx.author.mention, embed=embed, components=[Button("Add The Word", color="green", emoji="✅", disabled=True), Button("Cancel The Request", color="red", emoji="❌", disabled=True)])
            await ctx.send("Timeout")
    @addbw.error
    async def addbw_error(self, ctx, error):
      await ctx.send(notadmin(self))
    @commands.command(aliases=['blacklistedwordlist'], description='Get all blacklisted words', help="bwlist [all?]")
    @commands.has_permissions(administrator=True)
    async def bwlist(self, ctx, arg="no"):
      loaded=openfile()
      try:
        loaded[f"badword_{str(ctx.guild.id)}"]
      except:
        await ctx.send(f"{cross(self)} No words in the BW list")
      else:
        if arg.lower()=="all":
          words=f"` {dot(self)}  `".join(loaded[f"badword_{str(ctx.guild.id)}"])
          words=f"`{words}`"
          embed=discord.Embed(title="Badword List - All", description=words, color=discord.Color.green())
          embed.set_footer(text="If any of these words are included in a statement, the message is deleted, and the user is warned", icon_url=ctx.author.avatar_url)
          omessageid=await ctx.send(embed=embed, components=[Button("Delete All?", emoji="⚠️", color="red")])
          try:
            btn=await omessageid.wait_for("button", self.bot, timeout=30)
            if btn.author!=ctx.author:
              await btn.respond(content=self.bot.notauthor, hidden=True)
            else:
              messageid=await btn.respond(content=f"{dot(self)} Are you **absolutely** sure you want to delete all the bad words?\n\n**__Note__: This is irreversible**", components=[Button("Delete", color="red", emoji="🗑️"), Button("Cancel", color="green", emoji="❌")])
              try:
                btn=await messageid.wait_for("button", self.bot)
                if btn.author!=ctx.author:
                  await btn.respond(content=self.bot.notauthor, hidden=True)
                else:
                  if btn.component.label.lower()=="cancel":
                    await messageid.delete()
                  else:
                    embed=discord.Embed(title="Badword List - All(These All Have Been Deleted)", description=words, color=discord.Color.green())
                    embed.set_footer(text=f"You can add words again by running {self.bot.command_prefix}addbw", icon_url=ctx.author.avatar_url)
                    await messageid.delete()
                    await omessageid.edit(embed=embed, components=[Button("Deleted All These", emoji="⚠️", color="red", disabled=True)])
                    loaded.pop([f"badword_{str(ctx.guild.id)}"])
                    loaded.pop([f"whoadded_{str(ctx.guild.id)}"])
                    loaded.pop([f"timestamp_{str(ctx.guild.id)}"])
                    setvalue(loaded)
              except:
                pass
          except asyncio.TimeoutError:
            await omessageid.edit(embed=embed, components=[Button("Timeout To Delete", emoji="⚠️", color="red",   disabled=True)])
        else:
          total=len(loaded[f"badword_{str(ctx.guild.id)}"])
          page=0
          word=loaded[f"badword_{str(ctx.guild.id)}"][page]
          addedby=self.bot.get_user(loaded[f"whoadded_{str(ctx.guild.id)}"][page])
          stamp=loaded[f"timestamp_{str(ctx.guild.id)}"][page]  
          embed=discord.Embed(title=f"BadWord List - Word {page+1}/{total}", color=0x008CFF)
          embed.add_field(name=f"{dot(self)} Word", value=word, inline=False)
          embed.add_field(name=f"{dot(self)} Added By", value=f"{addedby.mention} `[{addedby}] ({addedby.id})`", inline=False)
          embed.add_field(name=f"{dot(self)} Added On", value=stamp, inline=False)
          embed.set_footer(text="Toggle Pages Using The Buttons Below")
          messageid=await ctx.send(embed=embed, components=[[Button("Previous Page", color="blurple", emoji="⬅️", disabled=True if page==0 else False), Button("Next Page", color="blurple", emoji="➡️", disabled=True if page+1==len(loaded[f"badword_{str(ctx.guild.id)}"]) else False)], Button("Seek To A Given Page", color="grey", emoji="🔎")])
          error=False
          while not error:
            try:
              btn=await messageid.wait_for("button", self.bot, timeout=30)
              if btn.author!=ctx.author:
                await btn.respond(content=self.bot.notauthor, hidden=True)
              else:
                if btn.component.label.lower()=="previous page":
                  page=page-1
                  word=loaded[f"badword_{str(ctx.guild.id)}"][page]
                  addedby=self.bot.get_user(loaded[f"whoadded_{str(ctx.guild.id)}"][page])
                  stamp=loaded[f"timestamp_{str(ctx.guild.id)}"][page]  
                  embed=discord.Embed(title=f"BadWord List - Word {page+1}/{total}", color=0x008CFF)
                  embed.add_field(name=f"{dot(self)} Word", value=word, inline=False)
                  embed.add_field(name=f"{dot(self)} Added By", value=f"{addedby.mention} `[{addedby}] ({addedby.id})`", inline=False)
                  embed.add_field(name=f"{dot(self)} Added On", value=stamp, inline=False)
                  embed.set_footer(text="Toggle Pages Using The Buttons Below")
                  await btn.respond()
                  await btn.message.edit(embed=embed, components=[[Button("Previous Page", color="blurple", emoji="⬅️", disabled=True if page==0 else False), Button("Next Page", color="blurple", emoji="➡️", disabled=True if page+1==len(loaded[f"badword_{str(ctx.guild.id)}"]) else False)], Button("Seek To A Given Page", color="grey", emoji="🔎")])
                elif btn.component.label.lower()=="next page":
                  page=page+1
                  word=loaded[f"badword_{str(ctx.guild.id)}"][page]
                  addedby=self.bot.get_user(loaded[f"whoadded_{str(ctx.guild.id)}"][page])
                  stamp=loaded[f"timestamp_{str(ctx.guild.id)}"][page]
                  embed=discord.Embed(title=f"BadWord List - Word {page+1}/{total}", color=0x008CFF)
                  embed.add_field(name=f"{dot(self)} Word", value=word, inline=False)
                  embed.add_field(name=f"{dot(self)} Added By", value=f"{addedby.mention} `[{addedby}] ({addedby.id})`", inline=False)
                  embed.add_field(name=f"{dot(self)} Added On", value=stamp, inline=False)
                  embed.set_footer(text="Toggle Pages Using The Buttons Below")
                  await btn.respond()
                  await btn.message.edit(embed=embed, components=[[Button("Previous Page", color="blurple", emoji="⬅️", disabled=True if page==0 else False), Button("Next Page", color="blurple", emoji="➡️", disabled=True if page+1==len(loaded[f"badword_{str(ctx.guild.id)}"]) else False)], Button("Seek To A Given Page", color="grey", emoji="🔎")])
                else:
                  def check(m):
                    return m.author==ctx.author and m.channel==ctx.channel
                  await btn.respond(content=f"{dot(self)} Enter the page number in the chat:", hidden=True)
                  try:
                    page=await self.bot.wait_for("message", check=check, timeout=30)
                  except asyncio.TimeoutError:
                    await ctx.send(f"{cross(self)} Timeout")
                    error=True
                    break
                  else:
                    page=page.content
                    try:
                      page=int(page)
                    except:
                      await ctx.send(f"{cross(self)} Not a valid page number")
                    else:
                      if page>len(loaded[f"badword_{str(ctx.guild.id)}"]):
                        await ctx.send(f"{cross(self)} Page out of index(Total Pages: {len(db['bw'])})")
                      else:
                        page=page-1
                        word=loaded[f"badword_{str(ctx.guild.id)}"][page]
                        addedby=self.bot.get_user(loaded[f"whoadded_{str(ctx.guild.id)}"][page])
                        stamp=loaded[f"timestamp_{str(ctx.guild.id)}"][page]
                        embed=discord.Embed(title=f"BadWord List - Word {page+1}/{total}", color=0x008CFF)
                        embed.add_field(name=f"{dot(self)} Word", value=word, inline=False)
                        embed.add_field(name=f"{dot(self)} Added By", value=f"{addedby.mention} `[{addedby}] ({addedby.id})`", inline=False)
                        embed.add_field(name=f"{dot(self)} Added On", value=stamp, inline=False)
                        embed.set_footer(text="Toggle Pages Using The Buttons Below")
                        await messageid.delete()
                        messageid=await ctx.send(embed=embed, components=[[Button("Previous Page", color="blurple", emoji="⬅️", disabled=True if page==0 else False), Button("Next Page", color="blurple", emoji="➡️", disabled=True if page+1==len(loaded[f"badword_{str(ctx.guild.id)}"]) else False)], Button("Seek To A Given Page", color="grey", emoji="🔎")])
            except asyncio.TimeoutError:
              error=True
              await messageid.reply(f"{cross(self)} Timeout")
          await messageid.edit(embed=embed, components=[[Button("Previous Page", color="blurple", emoji="⬅️", disabled=True), Button("Next Page", color="blurple", emoji="➡️", disabled=True)], Button("Seek To A Given Page", color="grey", emoji="🔎", disabled=True)])
    @bwlist.error
    async def bwlist_error(self, ctx, error):
      await ctx.send(notadmin(self))
    @commands.command(aliases=['blacklistedwordremove'], description='Remove A Blacklisted Word', help="removebw <word>")
    @commands.has_permissions(administrator=True)
    async def removebw(self, ctx, bw=None):
      loaded=openfile()
      try:
        loaded[f"badword_{str(ctx.guild.id)}"]
      except:
        await ctx.send(f"{cross(self)} No words in the list")
      else:
        if bw is None:
          await ctx.send(f"{cross(self)} No argument passed")
        elif bw not in loaded[f"badword_{str(ctx.guild.id)}"]:
          await ctx.send(f"{cross(self)} Word not found in list")
        else:
          messageid=await ctx.send(f"{dot(self)} Do you wish to confirm the fact that you want to remove `{bw}` from the list!", components=[Button("Confirm", color="green"), Button("Cancel", color="red")])
          try:
            btn=await messageid.wait_for("button", self.bot, timeout=30)
            if btn.component.label.lower()=="confirm":
              index=loaded[f"badword_{str(ctx.guild.id)}"].index(bw)
              loaded[f"badword_{str(ctx.guild.id)}"].pop(index)
              loaded[f"whoadded_{str(ctx.guild.id)}"].pop(index)
              loaded[f"timestamp_{str(ctx.guild.id)}"].pop(index)
              setvalue(loaded)
              await ctx.send(f"{tick(self)} Successfully removed `{bw}` from the list of prohibited words!")
              await btn.respond()
              await btn.message.edit(f"{tick(self)} Removed `{bw}` from the list!", components=[Button("Confirm", color="green", disabled=True), Button("Cancel", color="red", disabled=True)])
            else:
              await ctx.send(f"{cross(self)} Alright, lets pretend you never ran that..")
              await btn.respond()
              await btn.message.edit(f"{cross(self)} Cancelled removal of `{bw}` from the list!", components=[Button("Confirm", color="green", disabled=True), Button("Cancel", color="red", disabled=True)])
          except asyncio.TimeoutError:
            await ctx.send("Timeout")
            await messageid.delete()
    @removebw.error
    async def removebw_error(self, ctx, error):
      await ctx.send(notadmin(self))
    @commands.Cog.listener("on_message")
    async def on_message(self, message):
      loaded=openfile()
      try:
        loaded[f"badword_{message.guild.id}"]
      except:
        return
      else:
        try:
          loaded[f"ignorerole_{message.guild.id}"]
        except:
          roles=None
        else:
          roles=loaded[f"ignorerole_{message.guild.id}"]
        try:
          loaded[f"ignorechannel_{message.guild.id}"]
        except:
          channels=None
        else:
          channels=loaded[f"ignorechannel_{message.guild.id}"]
        check=False
        if roles is None:
          pass
        else:
          for i in message.author.roles:
            if i.id in roles:
              check=True
              break
            else:
              continue
        if not channels:
          pass
        else:
          if message.channel.id in channels:
            check=True
          else:
            pass
        if check:
          return
        elif message.author.bot:
          return
        elif message.author.guild_permissions.administrator:
          return
        else:
          wordsused=[]
          for i in loaded[f"badword_{message.guild.id}"]:
            if i.lower() in message.content.lower():
              wordsused.append(i)
          offenses=0 if len(wordsused)==0 else 0.5 if len(wordsused)==1 else int(len(wordsused)/2)
          if offenses==0:
            return
          else:
            try:
              loaded[f"cases_{message.guild.id}"]
            except:
              loaded[f"cases_{message.guild.id}"]=1
              setvalue(loaded)
            else:
              loaded[f"cases_{message.guild.id}"]+=1
              setvalue(loaded)
            if len(wordsused)==1:
              try:
                loaded[f"1_{message.author.id}_{message.guild.id}"]
              except: 
                loaded[f"1_{message.author.id}_{message.guild.id}"]=1
                setvalue(loaded)
                added=0
                isadded=f"\n{dot(self)} **Note:** Because of having only 1 swear word in the message, and not having any previous single swear word offenses in record(single word offenses are deleted after done twice, since a warn is added in that case), the user was not warned. If this repeats, then the single swear word offense will be set to 0, and they will be warned."
              else:
                loaded.pop([f"1_{message.author.id}_{message.guild.id}"])
                setvalue(loaded)
                try:
                  loaded[f"warns_{message.author.id}_{message.guild.id}"]
                except:
                  loaded[f"warns_{message.author.id}_{message.guild.id}"]=1
                  setvalue(loaded)
                  added=0
                  isadded=f"\n{dot(self)} **Note:** Although the user has only 1 swear word, they were warned because of the fact that they had another track record of a single swear world logged in the bot. This is now reset to 0, and 1 warn is added"
                else:
                  loaded[f"warns_{message.author.id}_{message.guild.id}"]+=1
                  setvalue(loaded)
                added=1
                isadded=f"\n{dot(self)} **Note:** Although the user has only 1 swear word, they were warned because of the fact that they had another track record of a single swear world logged in the bot. This is now reset to 0, and 1 warn is added"
            else:
              try:
                loaded[f"warns_{message.author.id}_{message.guild.id}"]
              except:
                loaded[f"warns_{message.author.id}_{message.guild.id}"]=offenses
                setvalue(loaded)
                added=offenses
                isadded=""
              else:
                loaded[f"warns_{message.author.id}_{message.guild.id}"]+=offenses
                setvalue(loaded)
                added=offenses
                isadded=""
            embed=discord.Embed(title="Usage Of Prohibited Words!", description=f"{cross(self)} {message.author.mention}, refrain from using blacklisted server words, and/or strong language.\n Words Used: `{len(wordsused)}` prohibited word{'s' if len(wordsused)!=1 else ''}. The words can be viewed in the logs(if you have enabled them).\n\n**Warns added:** `{added}`{isadded}", color=discord.Color.red())
            await message.delete()
            await message.channel.send(embed=embed)
            await asyncio.sleep(1)
            try:
              loaded[f"channel_{message.guild.id}"]
            except:
              return
            else:
              try:
                sendchannel=self.bot.get_channel(loaded[f"channel_{message.guild.id}"])
              except:
                return
              else:
                embed2=discord.Embed(title="Prohibited Words Used", description=f"{cross(self)} {message.author.mention} used the following words in {message.channel.mention}:\n`{'`, `'.join(wordsused)}`\n\n**Warns added:** `{added}`{isadded}", color=discord.Color.red())
                await sendchannel.send(embed=embed2)
    @commands.command(aliases=['blacklistedwordlogs'], description='Set a log channel for blacklisted words', help="bwlogs <channel mention>")
    @commands.has_permissions(administrator=True)
    async def bwlogs(self, ctx):
      channel=ctx.message.channel_mentions
      if not channel:
        await ctx.send(f"{cross(self)} Mention a channel!")
        return
      else:
        channel=ctx.message.channel_mentions[0]
        await ctx.send(f"{tick(self)} Successfully updated the logs channel to {channel.mention}!")
        loaded=openfile()
        loaded[f"channel_{str(ctx.guild.id)}"]=channel
        setvalue(loaded)
    @bwlogs.error
    async def bwlogs_error(self, ctx, error):
      await ctx.send(notadmin(self))
    @commands.command(aliases=['blacklistedwordstats'], description='Settings and stats of the blacklisted words commands', help="bwstats")
    @commands.has_permissions(administrator=True)
    async def bwstats(self, ctx):
      loaded=openfile()
      try:
        loaded[f"cases_{str(ctx.guild.id)}"]
      except:
        cases=0
      else:
        cases=loaded[f"cases_{str(ctx.guild.id)}"]
      try:
        loaded[f"channel_{str(ctx.guild.id)}"]
      except:
        channel=f"{cross(self)} Not Set Yet. Run `{self.bot.command_prefix}bwlogs` to do so"
      else:
        channel=self.bot.get_channel(loaded[f"channel_{str(ctx.guild.id)}"]).mention
      embed=discord.Embed(title="Prohibited Word Stats", description=f"{tick(self)} Here are some stats on the prohibited words", color=discord.Color.green())
      embed.add_field(name=f"{dot(self)} No.of Cases", value=cases)
      embed.add_field(name=f"{dot(self)} Logs Channel", value=channel)
      embed.timestamp=datetime.datetime.now()
      await ctx.send(embed=embed)
    @bwstats.error
    async def bwstats_error(self, ctx, error):
      await ctx.send(notadmin(self))
    @commands.command(aliases=['blacklistedwordignorerole'], description='Set roles that can bypass the blacklisted word checker. Note: This does not add a role. This sets all the mentioned roles to roles that bypass the checker.', help="bwignorerole <role mentions>")
    @commands.has_permissions(administrator=True)
    async def bwignorerole(self, ctx):
      if not ctx.message.role_mentions:
        try:
          loaded.pop([f"ignorerole_{str(ctx.guild.id)}"])
          setvalue(loaded)
        except:
          await ctx.send(f"{cross(self)} Cannot set the roles to none, because it already is none")
        else:
          await ctx.send(f"{tick(self)} Successfully set the ignored roles to None")
      else:
        roles=[]
        roles=[i.name for i in ctx.message.role_mentions]
        save=[j.id for j in ctx.message.role_mentions]
        loaded[f"ignorerole_{str(ctx.guild.id)}"]=save
        setvalue(loaded)
        await ctx.send(f"{tick(self)} Success! The roles that can now bypass the blacklisted word checker are: **{', '.join(roles)}**")
    @bwignorerole.error
    async def bwignorerole_error(self, ctx, error):
      await ctx.send(notadmin(self))
    @commands.command(aliases=['blacklistedwordignorechannel'], description='Set channels that ignore the blacklisted word checker. Note: This does not add a channel. This sets all the mentioned channels to channels that bypass the checker.', help="bwignorechannel <channels mention>")
    @commands.has_permissions(administrator=True)
    async def bwignorechannel(self, ctx):
      loaded=openfile()
      if not ctx.message.channel_mentions:
        try:
          loaded.pop([f"ignorechannel_{str(ctx.guild.id)}"])
          setvalue(loaded)
        except:
          await ctx.send(f"{cross(self)} Cannot set the channels to none, because it already is none")
        else:
          await ctx.send(f"{tick(self)} Successfully set the ignored channels to None")
      else:
        roles=[]
        roles=[f"#{i.name}" for i in ctx.message.channel_mentions]
        save=[j.id for j in ctx.message.channel_mentions]
        loaded[f"ignorechannel_{str(ctx.guild.id)}"]=save
        setvalue(loaded)
        await ctx.send(f"{tick(self)} Success! The channels that can now bypass the blacklisted word checker are: **{', '.join(roles)}**")
    @bwignorechannel.error
    async def bwignorechannel_error(self, ctx, error):
      await ctx.send(notadmin(self))
def setup(bot):
    bot.add_cog(BlacklistedWords(bot))
