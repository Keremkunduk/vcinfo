import discord
from discord import option
import asyncio
import random
from datetime import datetime
from datetime import date
from tkinter import *
from time import sleep as sl

armut = 926500179006353448

userid = 680117066740924443

client = discord.Bot()

global font 
font = 'Reddit Sans'

@client.event
async def on_ready():
    print("Ready\n")
    global guild
    guild = client.get_guild(910981204625457203)

@client.event
async def on_voice_state_update(member, before, after):
    today = str(date.today())
    output = None
    situation = '' #None
    is_keremk_here = False

    ch_name = str(after.channel)
    ch = after.channel
    if ch == None:
        ch = before.channel
    
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

#DELETE THIS-----------------------------

    if after.self_stream:
        situation = ' On Stream'
    elif before.self_stream:
        situation = ' Off Stream'
    if after.self_mute:
        situation = ' Muted'
    elif before.self_mute:
        situation = ' Unmuted'
    if after.self_deaf:
        situation = ' Deafen'
    elif before.self_deaf:
        situation = ' Undeafen'

    # if after.self_mute:
    #     situation = ' Muted'
    # elif before.self_mute:
    #     situation = ' Unmuted'
    # if after.self_deaf:
    #     situation = ' Deafen'
    # elif before.self_deaf:
    #     situation = ' Undeafen'
    # if after.self_stream:
    #     situation = ' On Stream'
    # elif before.self_stream:
    #     situation = ' Off Stream'

#-----------------------------------------

#IS KEREMK HERE

    for i in ch.members:
        if i.name == 'keremkunduk' and member.name != 'keremkunduk':
            is_keremk_here = True
    

    if not before.channel:
        output = str(member.name) + f' | Joined {ch_name}{situation}' + ' | ' + current_time + ' | ' + today

        if is_keremk_here:
            root = Tk()
            root.geometry("+0+0")
            root.overrideredirect(True)
            root.wm_attributes("-topmost", True)
            root.wm_attributes("-alpha", 0.01)
            root.resizable(0, 0)
            root.wm_attributes('-alpha', 0.7)
            display = Label(root, font=(font, 24, 'bold'), bg='black')
            display.config(text=f'{member.name} Joined', fg='cyan')
            display.pack()
            root.update()
            sl(2)
            root.destroy()
            root.update()

    if before.channel and after.channel:
        if str(before.channel) != str(ch_name): #if channels are same, then member didn't changed his channel, changed situation
            output = str(member.name) + f' | {before.channel} -> {ch_name}{situation}' + ' | ' + current_time + ' | ' + today

            for i in before.channel.members:
                if i.name == 'keremkunduk' and member.name != 'keremkunduk':
                    is_keremk_here = True

            if is_keremk_here:
                root = Tk()
                root.geometry("+0+0")
                root.overrideredirect(True)
                root.wm_attributes("-topmost", True)
                root.wm_attributes("-alpha", 0.01)
                root.resizable(0, 0)
                root.wm_attributes('-alpha', 0.7)
                display = Label(root, font=(font, 24, 'bold'), bg='black')
                # display.config(text=f'{member.name} {before.channel} -> {ch_name}', fg='cyan')
                display.config(text=f'{member.name} -> {ch_name}', fg='cyan')
                display.pack()
                root.update()
                sl(2)
                root.destroy()
                root.update()

        # elif after.self_mute:
            # situation = ' Muted'
        # elif before.self_mute:
            # situation = ' Unmuted'
        # if after.self_deaf:
            # situation = ' Deafen'
        # elif before.self_deaf:
            # situation = ' Undeafen'
        # if after.self_stream:
            # situation = ' On Stream'
        # elif before.self_stream:
            # situation = ' Off Stream'
    if before.channel and not after.channel:
        output = str(member.name) + f' | Left {before.channel}{situation}' + ' | ' + current_time + ' | ' + today #ch_name

        if is_keremk_here:
            root = Tk()
            root.geometry("+0+0")
            root.overrideredirect(True)
            root.wm_attributes("-topmost", True)
            root.wm_attributes("-alpha", 0.01)
            root.resizable(0, 0)
            root.wm_attributes('-alpha', 0.7)
            display = Label(root, font=(font, 24, 'bold'), bg='black')
            display.config(text=f'{member.name} Left', fg='cyan')
            display.pack()
            root.update()
            sl(2)
            root.destroy()
            root.update()

    if output == None:
        output = str(member.name) + ' |' + str(situation) + ' | ' + current_time + ' | ' + today
        if 'Stream' in situation or 'eafen' in situation:
            if is_keremk_here:
                root = Tk()
                root.geometry("+0+0")
                root.overrideredirect(True)
                root.wm_attributes("-topmost", True)
                root.wm_attributes("-alpha", 0.01)
                root.resizable(0, 0)
                root.wm_attributes('-alpha', 0.7)
                display = Label(root, font=(font, 24, 'bold'), bg='black')
                display.config(text=f'{member.name}{situation}', fg='cyan')
                display.pack()
                root.update()
                sl(2)
                root.destroy()
                root.update()
    
    print(output)
    op = open('vclog.txt', 'a', encoding='utf-8')
    op.write(output + '\n')
    op.close
    
    # if not before.channel and after.channel:
    #     kanalid = 1063747294215815230

    #     channel = client.get_channel(kanalid)
    #     members = channel.members
    #     if members != []:
    #         for x in members:
    #             if x.id == member.id:
    #                 print(f'{member} Bağlandı')
    #             else:
    #                 print(f'{member} Ayrıldı')
    #     else:
    #         print(f'{member} Ayrıldı')               

client.run('OTI2NTAwMTc5MDA2MzUzNDQ4.GHjtxl.-bP8dpb0hz8hAfc8QnrgEEZR9bgmINV208SQbs')