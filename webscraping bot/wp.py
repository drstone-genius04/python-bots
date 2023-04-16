import csv
import datetime
import pytz
import discord
from discord.ext import tasks, commands
client = discord.Client(intents=discord.Intents.default())

@tasks.loop(hours=24)
async def send_birthday_wishes():
    with open('birthday.csv', 'r') as file:
        reader = csv.reader(file)
        # next(reader) # skip header row
        for row in reader:
            name, dob, phone = row
            dt_now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            # print(dt_now, "sfdfdsg", dob)
            dob = datetime.datetime.strptime(dob, "%d/%m/%Y").replace(year=dt_now.year)
            if dob.date() == dt_now.date():
                message = f"Happy Birthday {name}! Click this link to send birthday wishes on Whatsapp: https://wa.me/{phone}?text=Happy%20Birthday%20{name}!"
                channel = client.get_channel(1096374826865791058) # replace with your channel ID
                await channel.send(message)

@client.event
async def on_ready():
    send_birthday_wishes.start()
    print('Bot is ready.')

client.run('MTA5NjM3MTg0NzUwMDY3MzA1Ng.GmE2iW.eXYDD52ULS4HBa9eLvwU7ynmBx4_KFyQmYPHyA')