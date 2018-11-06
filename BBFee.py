import discord
import asyncio
import os
from discord.ext import commands

Bot = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
        print('|-----------------------------------------------------------------------------')
        print('| # ME')
        print('| Name:     ' + bot.user.name)
        print('| ID:       ' + bot.user.id)
        print('| Discord:  ' + discord.__version__)
        print('| Invite:   https://discord.now.sh/' + bot.user.id + '?p1543892215')
        print('|-----------------------------------------------------------------------------')

@bot.command(pass_context=True)
async def fee(ctx, *, arg : int):
    if arg > 0:
        paypal = arg - (0.039 * arg + 0.030)
        ebay = arg - (0.129 * arg)
        stockx = arg - (0.125 * arg)
        goat = arg - (0.095 * arg + 5)
        grailed = arg - (0.089 * arg)

        embed=discord.Embed(title="Fee Calculator", color=0x942192)
        #embed.set_author(name="Bandit Fees")
        embed.add_field(name="PayPal", value="${}".format(paypal), inline=True)
        embed.add_field(name="eBay", value="${}".format(ebay), inline=False)
        embed.add_field(name="StockX", value="${}".format(stockx), inline=False)
        embed.add_field(name="Goat", value="${}".format(goat), inline=False)
        embed.add_field(name="Grailed", value="${}".format(grailed), inline=True)
        embed.set_footer(text="BanditBlock | Developed by users/me#0001")
        await bot.say(embed=embed)
        print('Fees Command Used by %s' % ctx.message.author.name)
    else:
        bot.say('Message')

bot.run('token')
