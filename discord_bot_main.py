import discord
from discord.ext import commands
import random
from credentials import *
from discord_bot_classes import *

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print('Logged In as:')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------------')
    create_table_player_ranks()
    create_table_ranks()
    create_table_crafting_datasheet()
    create_table_player_ign()
    print('-----------------')

@bot.command()
async def add_rank(*args):
    try:
        if len(args) > 1:
            rank = get_rank_description(args[0])
            if rank is None:
                add_rank_description(args[0], args[1])
                await bot.say('Rank ' + args[0] + ' was added successful')
            else:
                await bot.say('Rank ' + args[0] + ' already exists')
        else:
            await bot.say('Please enter the required arguments, or use /help command_name to check how to use the command')
    except Exception as e:
        print(e)

@bot.command(pass_context = True)
async def player_assign_rank(ctx, member: discord.Member, *args):
    try:
        if len(args) >= 0:
            rank = get_rank_description(args[0])
            if rank is not None:
                rank_name = args[0]
                rank_description = rank['rank_description']
                if member is not None:
                    add_player_rank(str(member), rank_name, rank_description)
                    await bot.say('Member ' + str(member) + ' assigned to rank ' + rank_name)
                else:
                    await bot.say('Discord member is not in the channel')
            else:
                await bot.say('Rank does not exist')
        else:
            await bot.say('Please enter the required arguments, or use /help command_name to check how to use the command')
    except Exception as e:
        print(e)

@bot.command(pass_context = True)
async def get_player_info(ctx, member: discord.Member):
    try:
        info = get_player_rank(str(member))
        rank_description = info['rank_description']
        ingame_name = info['ingame_name']
        rank = info['rank']
        await bot.say('Member ' + str(member) + ' is rank: ' + rank + ', with rank description: "' + rank_description + '" and IGN: ' +ingame_name)
    except Exception as e:
        print(e)

@bot.command(pass_context = True)
async def get_player_datasheet(ctx, member: discord.Member):
    try:
        datasheet = get_datasheet(str(member))
        await bot.say('Player ' + datasheet['ingame_name'] + ' datasheet: ' + datasheet['datasheet_url'])
    except Exception as e:
        print(e)

@bot.command(pass_context = True)
async def add_player_datasheet(ctx, member: discord.Member, *args):
    try:
        if len(args) > 1:
            if member is not None:
                add_datasheet(str(member), args[0], args[1])
                await bot.say('Datasheet added successful')
            else:
                await bot.say('There is no member with that name in discord channel')
        else:
            await bot.say(
                'Please enter the required arguments, or use /help command_name to check how to use the command')
    except Exception as e:
        print(e)


@bot.command()
async def get_rank_info(*args):
    try:
        if len(args) > 0:
            await bot.say(get_rank_description(args[0])['rank_description'])
        else:
            await bot.say('Please enter the required arguments, or use /help command_name to check how to use the command')
    except Exception as e:
        print(e)

@bot.command()
async def add_player_ign(member: discord.Member, *args):
    try:
        if len(args) >= 0:
            add_player_ingamename(str(member), args[0])
            await bot.say('Player ' + args[0] + ' added successfully')
        else:
            await bot.say('Please enter the required arguments, or use /help command_name to check how to use the command')
    except Exception as e:
        print(e)

@bot.command()
async def get_player_ign(member: discord.Member):
    try:
        if member is not None:
            player_ign = get_player_ingamename(str(member))['ingame_name']
            await bot.say('Player ' + str(member) + ' has IGN: ' + player_ign)
        else:
            await bot.say('Please enter the member name, or use /help command_name to check how to use the command')
    except Exception as e:
        print(e)

bot.run(TOKEN)