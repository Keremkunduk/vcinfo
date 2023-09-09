import discord
from discord import option
from datetime import datetime
from tkinter import *
from time import sleep as sl

token = None

guild_id = None
yourusername = None

client = discord.Bot()



@client.event
async def on_ready():
    print("Ready\n")
    global guild
    guild = client.get_guild(guild_id)

@client.event
async def on_voice_state_update(member, before, after):
    output = None
    situation = '' #None
    im_here = False

    ch_name = str(after.channel)
    ch = after.channel
    if ch == None:
        ch = before.channel
    
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    if after.self_mute:
        situation = ' Muted'
    elif before.self_mute:
        situation = ' Unmuted'
    if after.self_deaf:
        situation = ' Deafen'
    elif before.self_deaf:
        situation = ' Undeafen'
    if after.self_stream:
        situation = ' On Stream'
    elif before.self_stream:
        situation = ' Off Stream'

    for i in ch.members:
        if i.name == yourusername and member.name != yourusername:
            im_here = True
    

    if not before.channel:
        output = str(member.name) + f' | Joined {ch_name}{situation}' + ' | ' + current_time

        if im_here:
            root = Tk()
            root.geometry("+0+0")
            root.overrideredirect(True)
            root.wm_attributes("-topmost", True)
            root.wm_attributes("-alpha", 0.01)
            root.resizable(0, 0)
            root.wm_attributes('-alpha', 0.7)
            timer_display = Label(root, font=('Trebuchet MS', 24, 'bold'), bg='black')
            timer_display.config(text=f'{member.name} Joined', fg='red')
            timer_display.pack()
            root.update()
            sl(2)
            root.destroy()
            root.update()

    if before.channel and after.channel:
        if str(before.channel) != str(ch_name): #if channels are same, then member didn't changed his channel, changed situation
            output = str(member.name) + f' | {before.channel} -> {ch_name}{situation}' + ' | ' + current_time

            for i in before.channel.members:
                if i.name == yourusername and member.name != yourusername:
                    im_here = True

            if im_here:
                root = Tk()
                root.geometry("+0+0")
                root.overrideredirect(True)
                root.wm_attributes("-topmost", True)
                root.wm_attributes("-alpha", 0.01)
                root.resizable(0, 0)
                root.wm_attributes('-alpha', 0.7)
                timer_display = Label(root, font=('Trebuchet MS', 24, 'bold'), bg='black')
                # timer_display.config(text=f'{member.name} {before.channel} -> {ch_name}', fg='red')
                timer_display.config(text=f'{member.name} -> {ch_name}', fg='red')
                timer_display.pack()
                root.update()
                sl(2)
                root.destroy()
                root.update()

    if before.channel and not after.channel:
        output = str(member.name) + f' | Left {before.channel}{situation}' + ' | ' + current_time #ch_name

        if im_here:
            root = Tk()
            root.geometry("+0+0")
            root.overrideredirect(True)
            root.wm_attributes("-topmost", True)
            root.wm_attributes("-alpha", 0.01)
            root.resizable(0, 0)
            root.wm_attributes('-alpha', 0.7)
            timer_display = Label(root, font=('Trebuchet MS', 24, 'bold'), bg='black')
            timer_display.config(text=f'{member.name} Left', fg='red')
            timer_display.pack()
            root.update()
            sl(2)
            root.destroy()
            root.update()

    if output == None:
        output = str(member.name) + ' |' + str(situation) + ' | ' + current_time
        if 'Stream' in situation or 'eafen' in situation:
            if im_here:
                root = Tk()
                root.geometry("+0+0")
                root.overrideredirect(True)
                root.wm_attributes("-topmost", True)
                root.wm_attributes("-alpha", 0.01)
                root.resizable(0, 0)
                root.wm_attributes('-alpha', 0.7)
                timer_display = Label(root, font=('Trebuchet MS', 24, 'bold'), bg='black')
                timer_display.config(text=f'{member.name}{situation}', fg='red')
                timer_display.pack()
                root.update()
                sl(2)
                root.destroy()
                root.update()
    
    print(output)
    op = open('vclog.txt', 'a')
    op.write(output + '\n')
    op.close

client.run(token)