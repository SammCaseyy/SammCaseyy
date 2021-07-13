import random

import discord

from discord.ext import commands

client = commands.Bot(command_prefix=".")


@client.event
async def on_boot():
    print("Bot is ready! ")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Rust'))


@client.event
async def on_member_join(member):
    await on_member_join.send(f'member has joined the server.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.event
async def on_member_remove():
    await ctx.send(f'member has left a server.')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.', ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def i(ctx):
    await ctx.send('Commands: .ping .kick .ban, .inf8ball, sleep, wake *Note Kick and Ban commands are restricted!')


@client.command()
async def kick(ctx, reason: None):
    await discord.member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')


@client.command()
async def inf8ball(ctx):
    await ctx.send(f'8ball will answer your most desired questions, simply type .8ball and your question and you '
                   f'will get an answer.')


@client.command()
async def sleep(ctx):
    await ctx.send(f'Bot powering down')
    await client.change_presence(activity=discord.Game('Sleep'))


@client.command()
async def wake(ctx):
    await ctx.send(f'Bot powering up')
    await client.change_presence(activity=discord.Game('.help for commands'))


@client.command()
async def plug(ctx):
    await ctx.send("https://discord.gg/Aa6JA8D")


@client.event
async def clear(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('please pass in all required arguments')


client.run("Njg5ODA4NjEyNTI0Mjk0MjM4.XnIQVQ.GUFj4VDnpemiuWNKdUQNt2tJ1HE")
