import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import datetime
import random
import json
import asyncio
def openfile():
    with open("db.json", "r") as f:
        return json.load(f)
def setvalue(loaded):
    with open("db.json", "w") as f:
        json.dump(loaded, f, indent=4)
def setvar(var, user, value):
    loaded=openfile()
    try:
        result=loaded[f"{var}_{str(user.id)}"]
    except:
        loaded[f"{var}_{str(user.id)}"]=value
        setvalue(loaded)
    else:
        pass
def setboxes(ctx):
      setvar("norm", ctx.author, 0)
      setvar("nicebox", ctx.author, 0)
      setvar("bigtrunk", ctx.author, 0)
      setvar("literalchristmasbox", ctx.author, 0)
def member(guild, arg, author):
  if arg is None:
    return author
  else:
    arg=arg.lower()
    member=None
    for i in guild.members:
      if arg in i.name.lower() or arg==str(i.id):
        member=i
        break
      else:
        continue
    return member or author
def getitem(ctx, item):
    loaded=openfile()
    itemcount=loaded[f"{item}_{str(ctx.author.id)}"]
    return f"— {itemcount} Owned"
def snowball(self):
  return self.bot.get_emoji(919480202625712168)
def candy(self):
  return self.bot.get_emoji(919601596575391815)
def box(self):
  return self.bot.get_emoji(919608196270809159)
def norm(self):
  return self.bot.get_emoji(919608196270809159)
def workemoji(self):
  return self.bot.get_emoji(919930073056968704)
def nicebox(self):
  return self.bot.get_emoji(920173147595100241)
def bigtrunk(self):
  return self.bot.get_emoji(920173641654730762)
def literalchristmasbox(self):
  return self.bot.get_emoji(920174948889292800)
def snowglobes(self):
  return self.bot.get_emoji(919930535546060800)
def christmastree(self):
  return self.bot.get_emoji(919479797728542771)
def magichat(self):
  return self.bot.get_emoji(921002072344768512)
def santa(self):
  return self.bot.get_emoji(921003878349160488)
def chocolate(self):
  return self.bot.get_emoji(921002740765831189)
def jinglebells(self):
    return self.bot.get_emoji(921003339779538975)
def reindeer(self):
    return self.bot.get_emoji(921001573612662794)
def getcolor():
  return random.choice([0x00216F, 0xF2F2F2, 0xE40A2D, 0x165B33])
def tagline():
  choice=["Be festive, it’s Christmas here!","Time for the mistletoe","Is it too late to be good?","Classy Christmas, huh?","On the way to Santa’s good list!","Santa is real, fun is surreal!","Make it a December to Remember!","Hope your Christmas is perfect!","Feel the magic of Christmas!","Merry Christmas!","It's Christmas time, let's cheer up and have fun!","Spread joy and love, it's the Christmas season!","Let's spread the festive spirit, it's Christmas time!","Be festive; it’s Christmas here!","Spread the spirit of X’mas!","Let joy and light fill our lives on Christmas!","Christmas is the season of light; make your houses bright!","It’s Christmas time; let’s spread love!","On Christmas Day let joy suffuse our lives!","Dear Santa, I’ve been good","Let it snow, let it snow, let it snow","Hurray! It’s Christmas","Be jolly in the festive season!","Christmas isn’t a season. It’s a feeling","Welcome Christmas into your heart"]
  return random.choice(choice)
def icon():
  choice=["https://media.discordapp.net/attachments/879257566289494076/919610547211755540/2Q.png","https://i.natgeofe.com/k/dfc7bec2-0657-4887-81a7-6d024a8c3f70/WH-XmasTree.jpg","https://nationaltoday.com/wp-content/uploads/2019/12/christmas-1-640x514.jpg","https://media.istockphoto.com/photos/christmas-tree-with-baubles-and-blurred-shiny-lights-picture-id1179032100?k=20&m=1179032100&s=612x612&w=0&h=GY7SDX2_9vECRjbvcR0DDp6s3hGV0l8VijMMkJvudTU=","https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/e1d26590136839.5e0ee5755b5e8.gif","https://www.icegif.com/wp-content/uploads/christmas-icegif-45.gif","https://cdn.dribbble.com/users/1448034/screenshots/5635128/christmas01.gif","https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/401d1c59877301.5a326a7ad0fd8.gif","https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/74aac789715791.5dfd5cc945094.gif","https://acegif.com/wp-content/gif/merrychristmas-unq-4.gif","https://cdna.artstation.com/p/assets/images/images/008/620/676/original/evgenii-barankin-santa-crist.gif?1513976231","https://cdn.dribbble.com/users/1429256/screenshots/9196528/media/d43fe1064499f9b78fa7467e0f201315.gif","https://www.sendagifty.com/storage/gif_images/q2QrkQHEgIWbl2u9qz8RU33WWVc5o3VHwyVe4BeZ.gif","https://acegif.com/wp-content/gif/mercs15ddn-44.gif","https://i.pinimg.com/originals/06/71/5b/06715ba633ee1b0a343ffb26a7d85972.gif"]
  return random.choice(choice)
def randomsnowball(self, ctx, user):
  if random.randrange(1,6)==1:
    setvar("snowball", user, 0)
    randnum=random.randrange(1,30)
    loaded=openfile()
    if randnum==15:
      loaded[f"snowball_{str(user.id)}"]+=10
      setvalue(loaded)
      return f"You found {snowball(self)} **10** snowballs!"
    elif randnum<=5:
      loaded[f"snowball_{str(user.id)}"]+=5
      setvalue(loaded)
      return f"You found {snowball(self)} **5** snowballs!"
    else:
      add=random.randrange(1,4)
      loaded[f"snowball_{str(user.id)}"]+=add
      setvalue(loaded)
      return f"You found {snowball(self)} {add} snowball{'s' if add!=1 else ''}!"
  else:
    return ''


class ChristmasEconomy(commands.Cog): 
    """Commands Related To Christmas Economy"""
    def __init__(self, bot):
      self.bot=bot
    @commands.command(description="Get The Items In The Inventory Of You/A Given User!", help="inv [member]", aliases=["inventory","lab","bal"])
    @commands.cooldown(1, 5, BucketType.user)
    async def inv(self, ctx, arg=None):
      try:
        user=ctx.message.mentions[0]
      except:
        user=member(ctx.guild, arg, ctx.author)
      anycontent=randomsnowball(self, ctx, ctx.author)
      setvar("snowball", user, 0)
      setvar("candy", user, 0)
      setvar("norm", user, 0)
      setvar("nicebox", user, 0)
      setvar("bigtrunk", user, 0)
      setvar("literalchristmasbox", user, 0)
      setvar("reindeer", user, 0)
      setvar("jinglebells", user, 0)
      setvar("christmastree", user, 0)
      setvar("snowglobes", user, 0)
      setvar("santa", user, 0)
      setvar("magichat", user, 0)
      setvar("chocolate", user, 0)
      loaded=openfile()
      sb=loaded[f"snowball_{str(user.id)}"]
      sendmessage=[]
      for i in ['candy','norm','nicebox','bigtrunk','literalchristmasbox','chocolate','jinglebells','magichat','snowglobes','christmastree','reindeer','santa']:
        toload=f"{i}_{str(user.id)}"
        sendmessage.append(f"{eval(i+'(self)')} `{loaded[toload]}` **{i}**")
      sendmessage="\n".join(sendmessage)
      msg=f"__Note:__ {user.mention} can convert these {snowball(self)} `{sb}` **snowball{'s' if sb!=1 else ''}** into {candy(self)} {int((sb-(sb%5))/5)} cand{'ies' if int((sb-(sb%5)))/5!=1 else 'y'}, with {snowball(self)} {sb%5} snowball{'s' if sb%5!=1 else ''} remaining as spare, if they desire to do so. They can later be used to buy items in the shop {box(self)}"
      embed=discord.Embed(description=f"**__Here's What's In The Inventory Of {user.mention}:__**\n{snowball(self)} `{sb}` **snowball{'s' if sb!=1 else ''}**\n{sendmessage}\n\n{'' if sb<5 else msg}", color=getcolor())
      embed.set_author(name=user, icon_url=user.avatar_url)
      embed.timestamp=datetime.datetime.now()
      embed.set_footer(text=tagline(), icon_url=self.bot.user.avatar_url)
      embed.set_thumbnail(url=icon())
      await ctx.send(embed=embed, content=anycontent)
    @inv.error
    async def inv_error(self, ctx, error):
      embed=discord.Embed(title="On A Cooldown", description=f"{ctx.author.mention}, you are on a cooldown of **{round(error.retry_after, 2)} seconds**. You can use the {box(self)} inv command every **10 seconds**, to prevent abuse", color=getcolor())
      embed.set_thumbnail(url=icon())
      embed.timestamp=datetime.datetime.now()
      await ctx.send(embed=embed)
    @commands.command(description="Go To Work(As A Santa By Default) And Earn Snowballs/Rewards!", help="work", aliases=["job"])
    @commands.cooldown(1, 3600, BucketType.user)
    async def work(self, ctx):
      add=random.randrange(10, 30)
      content=randomsnowball(self, ctx, ctx.author)
      candnum=0
      loaded=openfile()
      if random.randrange(0,11)==10:
        if random.randrange(1,12)==11:
          candnum=2
        else:
          candnum=1
        try:
          loaded[f"candy_{str(ctx.author.id)}"]
        except:
          loaded[f"candy_{str(ctx.author.id)}"]=candnum
          setvalue(loaded)
        else:
          loaded[f"candy_{str(ctx.author.id)}"]+=candnum
          setvalue(loaded)
      msg=f"\n\nWow! While working so hard, you incidentally found {candy(self)} **{candnum} cand{'ies' if candnum!=1 else 'y'}**! Congrats!!! {box(self)}"
      embed=discord.Embed(title=f"{workemoji(self)} Work", description=f"Working as a Santa, you sailed across the {snowglobe(self)} globe, chanting **ho ho ho**, and were rewarded {snowball(self)} **{add} snowballs** for your dedicated work!{msg if candnum!=0 else ''}", color=getcolor())
      loaded[f"snowball_{str(ctx.author.id)}"]+=add
      setvalue(loaded)
      embed.set_footer(text=tagline(), icon_url=self.bot.user.avatar_url)
      embed.set_thumbnail(url=icon())
      await ctx.send(embed=embed, content=content)
    @work.error
    async def work_error(self, ctx, error):
      embed=discord.Embed(title="On A Cooldown", description=f"{ctx.author.mention}, you are on a cooldown of **{round(error.retry_after, 2)} seconds**. You can use the {box(self)} work command every **1 hour**, to prevent abuse!", color=getcolor())
      embed.set_thumbnail(url=icon())
      embed.timestamp=datetime.datetime.now()
      await ctx.send(embed=embed)
    @commands.command(description="Exchange Your Snowballs For Candies(5:1)", help="exchange [how many(1)]", aliases=["convert"])
    @commands.cooldown(1, 120, BucketType.user)
    async def exchange(self, ctx, howmany=1):
      loaded=openfile()
      try:
        howmany=int(howmany)
      except:
        await ctx.send("Invalid number provided to convert")
        return
      else:
        snowballs=loaded[f"snowball_{str(ctx.author.id)}"]
        sendmessage=f"\n\nYou can at most exchange {snowball(self)} **{snowballs} snowballs** for {candy(self)} **{int((snowballs-(snowballs%5))/5)} cand{'ies' if int((snowballs-(snowballs%5))/5)!=1 else 'y'}**. If you exchange them all, you shall have {snowball(self)} **{snowballs%5} snowball{'s' if snowballs%5!=1 else ''}** remaining!"
        if howmany*5>snowballs:
          await ctx.send(f"You cannot exchange {snowball(self)} **{snowballs} snowball{'s' if snowballs!=1 else ''}** to {candy(self)} **{howmany} cand{'ies' if howmany!=1 else 'y'}**, that's literally illegal. You are {snowball(self)} **{(howmany*5)-snowballs} snowball{'s' if (howmany*5)-snowballs!=1 else ''}** short to be able to do that.{'' if snowballs<5 else sendmessage}")
        else:
          snowballs=howmany*5
          try:
            loaded[f"candy_{str(ctx.author.id)}"]
          except:
            loaded[f"candy_{str(ctx.author.id)}"]=howmany
            setvalue(loaded)
          else:
            loaded[f"candy_{str(ctx.author.id)}"]+=howmany
            setvalue(loaded)
          loaded[f"snowball_{str(ctx.author.id)}"]-=snowballs
          setvalue(loaded)
          await ctx.send(f"{ctx.author.mention}, I successfully exchanged {snowball(self)} **{snowballs} snowballs** of yours with {candy(self)} **{howmany} cand{'ies' if howmany!=1 else 'y'}**!")
    @exchange.error
    async def exchange_error(self, ctx, error):
      if isinstance(error, commands.BadArgument):
        await ctx.send(f"Bad argument! You need to supply a valid number of {candy(self)} candies to convert! If you do not supply any number, I automatically consider it to be 1.")
      else:
        embed=discord.Embed(title="On A Cooldown", description=f"{ctx.author.mention}, you are on a cooldown of **{round(error.retry_after, 2)} seconds**. You can use the {box(self)} exchange command every **2 minutes**, to prevent abuse!", color=getcolor())
        embed.set_thumbnail(url=icon())
        embed.timestamp=datetime.datetime.now()
        await ctx.send(embed=embed)
    @commands.command(description="Get The Items In The Shop!", help="shop", aliases=["store"])
    async def shop(self, ctx):
      loaded=openfile()
      content=randomsnowball(self, ctx, ctx.author)
      setboxes(ctx)
      with open("db.json", "r") as f:
          loaded=json.load(f)
      normc=loaded[f"norm_{str(ctx.author.id)}"]
      niceboxc=loaded[f"nicebox_{str(ctx.author.id)}"]
      bigtrunkc=loaded[f"bigtrunk_{str(ctx.author.id)}"]
      literalchristmasboxc=loaded[f"literalchristmasbox_{str(ctx.author.id)}"]
      try:
        loaded[f"candy_{str(ctx.author.id)}"]
      except:
        loaded[f"candy_{str(ctx.author.id)}"]=0
        setvalue(loaded)
        candyc=0
      else:
        candyc=loaded[f"candy_{str(ctx.author.id)}"]
      embed=discord.Embed(title="Shop", description=f"{candy(self)} **Candy** {'' if candyc==0 else getitem(ctx, 'candy')}\n(Run `{self.bot.command_prefix}exchange` to exchange {candy(self)} `1 Candy` for {snowball(self)} `5 Snowballs`)\n\n{box(self)} **Santa's Norm Gift** {'' if normc==0 else getitem(ctx, 'norm')}\n(Can be bought with {candy(self)} `2 candies`)\n\n{nicebox(self)} **Santa's Nice Box** {'' if niceboxc==0 else getitem(ctx, 'nicebox')}\n(Can be bought with {candy(self)} `5 Candies`)\n\n{bigtrunk(self)} **Santa's Big Trunk** {'' if bigtrunkc==0 else getitem(ctx, 'bigtrunk')}\n(Can be bought with {candy(self)} `10 Candies`)\n\n{literalchristmasbox(self)} **Literal Santa** {'' if literalchristmasboxc==0 else getitem(ctx, 'literalchristmasbox')}\n(Can be bought with {candy(self)} `20 Candies`)", color=getcolor())
      embed.set_footer(text=tagline(), icon_url=ctx.author.avatar_url)
      embed.set_thumbnail(url=icon())
      await ctx.send(embed=embed, content=content)
    @commands.command(description="Buy An Item From The Shop!", help="buy <amount> <item>", aliases=["purchase"])
    @commands.cooldown(1, 10, BucketType.user)
    async def buy(self, ctx, amount: int, item=None):
        if item is None:
            await ctx.send("Item not provided")
            return
        else:
          item=item.lower()
          found=False
          for i in ['norm', 'nicebox', 'bigtrunk', 'literalchristmasbox']:
            if item in i:
                item=i
                found=True
                break
            else:
                continue
          if not found:
            await ctx.send("Item not found")
            return
          else:
            list={
            'norm': 2,
            'nicebox': 5,
            'bigtrunk': 10,
            'literalchristmasbox': 20
            }
            cost=list[item]*amount
            setvar('snowball', ctx.author, 0)
            setvar('candy', ctx.author, 0)
            loaded=openfile()
            candies=loaded[f"candy_{str(ctx.author.id)}"]
            emoji=box(self) if item=='norm' else nicebox(self) if item=='nicebox' else bigtrunk(self) if item=='bigtrunk' else literalchristmasbox(self)
            if cost>candies:
                await ctx.send(f"You do not have enough {candy(self)} candies to buy {emoji} `{amount}` **{item}**! If you wish to buy it, you need {candy(self)} `{cost-candies}` candies more!")
                return
            else:
                setvar(item, ctx.author, 0)
                loaded=openfile()
                loaded[f"{item}_{str(ctx.author.id)}"]+=1
                loaded[f"candy_{str(ctx.author.id)}"]-=cost
                setvalue(loaded)
                await ctx.send(f"You successfully brought {emoji} `{amount}` **{item} box{'' if amount==1 else 'es'}**, and paid {candy(self)} `{cost}` candies to buy it!")
    @buy.error
    async def buy_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed=discord.Embed(title="On A Cooldown", description=f"{ctx.author.mention}, you are on a cooldown of **{round(error.retry_after, 2)} seconds**. You can use the {box(self)} buy command every **10 seconds**, to prevent abuse", color=getcolor())
            embed.set_thumbnail(url=icon())
            embed.timestamp=datetime.datetime.now()
            await ctx.send(embed=embed)
        else:
          await ctx.send(f"Please provide proper arguments! `{self.bot.command_prefix}buy <how many> <item>`")
    @commands.command(description="Use A Box And Get Items!", help="use <box name>", aliases=["open","box"])
    @commands.cooldown(1, 10, BucketType.user)
    async def use(self, ctx, amount: int, item=None):
        if item is None:
            await ctx.send("Item not provided")
            return
        else:
          item=item.lower()
          found=False
          for i in ['norm', 'nicebox', 'bigtrunk', 'literalchristmasbox']:
            if item in i:
                item=i
                found=True
                break
            else:
                continue
          if not found:
            await ctx.send("Item not found")
            return
          loaded=openfile()
          setvar(item, ctx.author, 0)
          if loaded[f"{item}_{str(ctx.author.id)}"]<amount:
                await ctx.send(f"You do not have {eval(item+'(self)')} `{amount}` **{item}**!")
          elif 20<amount:
            await ctx.send("You can open only 20 of any boxes at once!")
          else:
            loaded[f"{item}_{str(ctx.author.id)}"]-=amount
            setvalue(loaded)
            ucitems={
            'norm': ["snowball","snowball","snowball","snowball","snowball","snowball","snowball","snowball","candy","candy","snowball","snowball","snowball","candy","snowball","snowball","snowball","snowball","snowball","snowball","snowball"],
            'nicebox': ["snowball","snowball","candy","snowball","snowball","snowball","snowball","snowball","candy","candy","snowball","snowball","snowball","candy","snowball","snowball","snowball","snowball","candy","snowball","snowball"],
            'bigtrunk': ["snowball","candy","candy","snowball","snowball","snowball","snowball","snowball","candy","candy","snowball","candy","snowball","candy","snowball","snowball","snowball","candy","candy","snowball","snowball"],
            'literalchristmasbox': ["snowball","candy","candy","candy","snowball","snowball","candy","snowball","candy","candy","snowball","candy","snowball","candy","snowball","snowball","snowball","candy","candy","snowball","candy"]
            }
            ucitemschances={
            'norm': [1,1,1,1,1,1,1,1,1,1,2,3,1,2,1,1,1,2,2,2,1],
            'nicebox': [2,2,1,2,3,3,3,2,1,1,3,3,3,1,3,2,2,4,2,2,3],
            'bigtrunk': [3,1,2,3,3,3,4,3,2,1,3,2,3,2,3,3,3,2,1,4,5],
            'literalchristmasbox': [6,2,2,1,5,5,2,4,2,1,5,3,6,3,5,5,7,3,2,6,3]
            }
            citems={
            'norm': ["chocolate","chocolate","chocolate","jinglebells","jinglebells","jinglebells","chocolate","magichat","magichat","jinglebells","chocolate","magichat","chocolate","magichat","jinglebells"],
            'nicebox': ["chocolate","chocolate","jinglebells","jinglebells","snowglobes","jinglebells","chocolate","magichat","snowglobes","magichat","jinglebells","chocolate","snowglobes","magichat","magichat","jinglebells","jinglebells","jinglebells","snowglobes","snowglobes","snowglobes"],
            'bigtrunk': ["chocolate","snowglobes","christmastree","jinglebells","jinglebells","snowglobes","christmastree","jinglebells","chocolate","magichat","snowglobes","christmastree","magichat","snowglobes","chocolate","snowglobes","christmastree","magichat","magichat","jinglebells","jinglebells","christmastree","snowglobes","snowglobes","snowglobes","christmastree","christmastree"],
            'literalchristmasbox': ["chocolate","reindeer","snowglobes","reindeer","christmastree","jinglebells","jinglebells","snowglobes","christmastree","jinglebells","snowglobes","magichat","snowglobes","christmastree","magichat","reindeer","snowglobes","christmastree","reindeer","snowglobes","christmastree","magichat","magichat","jinglebells","jinglebells","reindeer","christmastree","snowglobes","snowglobes","snowglobes","christmastree","christmastree","reindeer","santa","santa","santa","reindeer","magichat"] 
            }
            citemschances={
            'norm': [1,2,1,1,1,2,1,1,1,2,3,1,2,1,1],
            'nicebox': [2,2,1,1,1,2,3,2,1,1,2,4,1,1,2,1,2,1,1,1,2],
            'bigtrunk': [4,2,2,2,2,1,1,3,5,3,2,1,2,2,2,2,1,1,2,3,3,2,1,2,3,1,1],
            'literalchristmasbox': [6,2,3,1,2,4,4,3,3,2,2,4,2,3,2,1,3,4,1,3,3,4,5,5,6,1,3,2,4,5,3,4,1,1,1,1,1,4]
            }
            loaded=openfile()
            earnt=[0, 0, 0, 0, 0, 0, 0, 0, 0]
            data=['snowball','candy','chocolate','jinglebells','magichat','snowglobes','christmastree','reindeer','santa']
            for i in range(0, amount):
                  rand=random.randrange(len(ucitems[item]))
                  thistimeitem=ucitems[item][rand]
                  thistimeitemcount=ucitemschances[item][rand]
                  setvar(thistimeitem, ctx.author, 0)
                  loaded=openfile()
                  loaded[f"{thistimeitem}_{str(ctx.author.id)}"]+=thistimeitemcount
                  setvalue(loaded)
                  earnt[data.index(thistimeitem)]+=thistimeitemcount
                  rand=random.randrange(len(citems[item]))
                  thistimeitem=citems[item][rand]
                  thistimeitemcount=citemschances[item][rand]
                  setvar(thistimeitem, ctx.author, 0)
                  loaded=openfile()
                  loaded[f"{thistimeitem}_{str(ctx.author.id)}"]+=thistimeitemcount
                  setvalue(loaded)
                  earnt[data.index(thistimeitem)]+=thistimeitemcount
            setvalue(loaded)
            embed=discord.Embed(title=f"Opening {eval(item+'(self)')} {amount} {item}", description="Sit tight, lemme check what was inside your box :eyes:", color=getcolor())
            embed.set_footer(text=tagline(), icon_url=ctx.author.avatar_url)
            messageid=await ctx.send(embed=embed)
            await asyncio.sleep(3)
            itemsgained=[f"{snowball(self)} `{earnt[0]}` Snowballs", f"{candy(self)} `{earnt[1]}` Candy", f"{chocolate(self)} `{earnt[2]}` Chocolate", f"{jinglebells(self)} `{earnt[3]}` Jingle Bells", f"{magichat(self)} `{earnt[4]}` Santashat", f"{snowglobes(self)} `{earnt[5]}` Snow Globes", f"{christmastree(self)} `{earnt[6]}` Christmas Tree", f"{reindeer(self)} `{earnt[7]}` Reindeer", f"{santa(self)} `{earnt[8]}` Santa"]
            sendmessage=[]
            imon=0
            for i in earnt:
                if i!=0:
                    sendmessage.append(itemsgained[imon])
                imon+=1
            embed=discord.Embed(title=f"Contents Of {eval(item+'(self)')} {amount} {item}", description="\n".join(sendmessage), color=getcolor())
            embed.set_thumbnail(url=icon())
            embed.set_footer(text="Ooooo", icon_url=ctx.author.avatar_url)
            await messageid.edit(embed=embed)
    @use.error
    async def use_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed=discord.Embed(title="On A Cooldown", description=f"{ctx.author.mention}, you are on a cooldown of **{round(error.retry_after, 2)} seconds**. You can use the {box(self)} inv command every **10 seconds**, to prevent abuse", color=getcolor())
            embed.set_thumbnail(url=icon())
            embed.timestamp=datetime.datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Please provide proper arguments! `{self.bot.command_prefix}use <how many> <item>`")
    @commands.command(aliases=['share','donate'], description='Give An Item To A User', help="give <amount> <item> <user>")
    @commands.cooldown(1, 10, BucketType.user)
    async def give(self, ctx, amount: int, item, arg):
        try:
            user=ctx.message.mentions[0]
        except:
          user=member(ctx.guild, arg, ctx.author)
        item=item.lower()
        found=False
        for i in ['norm', 'nicebox', 'bigtrunk', 'literalchristmasbox', 'snowball','candy','chocolate','jinglebells','magichat','snowglobes','christmastree','reindeer','santa']:
            if item in i:
                item=i
                found=True
                break
            else:
                continue
        if not found:
            await ctx.send("Item not found")
            return
        else:
            setvar(item, ctx.author, 0)
            setvar(item, user, 0)
            loaded=openfile()
            if user==ctx.author:
                await ctx.send("Giving yourself stuff, huh?")
                return
            elif amount>loaded[f"{item}_{str(ctx.author.id)}"]:
                await ctx.send("You cannot give more than you have!")
            else:
                loaded[f"{item}_{str(ctx.author.id)}"]-=amount
                loaded[f"{item}_{str(user.id)}"]+=amount
                setvalue(loaded)
                loaded=openfile()
                receiverhas=loaded[f"{item}_{str(user.id)}"]
                memberhas=loaded[f"{item}_{str(ctx.author.id)}"]
                await ctx.send(f"Successfully gave {eval(item+'(self)')} `{amount}` **{item}** to **{user}**! They now have {eval(item+'(self)')} `{receiverhas}` **{item}**, and you have {eval(item+'(self)')} `{memberhas}` **{item}** left!")
    @give.error
    async def give_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed=discord.Embed(title="On A Cooldown", description=f"{ctx.author.mention}, you are on a cooldown of **{round(error.retry_after, 2)} seconds**. You can use the {box(self)} give command every **10 seconds**, to prevent abuse", color=getcolor())
            embed.set_thumbnail(url=icon())
            embed.timestamp=datetime.datetime.now()
            await ctx.send(embed=embed)
        else:
          await ctx.send(f"Please provide proper arguments! `{self.bot.command_prefix}give <how many> <item> <member>`")
def setup(bot):
    bot.add_cog(ChristmasEconomy(bot))
