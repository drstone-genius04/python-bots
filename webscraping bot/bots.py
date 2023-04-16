import csv
import datetime
import pytz
import discord
import sqlite3

from discord.ext import tasks, commands

client = discord.Client(intents=discord.Intents.default())

# Connect to the database
conn = sqlite3.connect('imdb_data.db')

@tasks.loop(hours=24)
async def send_birthday_wishes():
    with open('birthday.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # skip header row
        for row in reader:
            name, dob, phone = row
            dt_now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            dob = datetime.datetime.strptime(dob, '%d/%m/%Y').replace(year=dt_now.year)
            if dob.date() == dt_now.date():
                # Retrieve the top rated movie from the database for the person's birth year
                cur = conn.cursor()
                cur.execute(f"SELECT title FROM imdb_data WHERE year='{dob.year}' ORDER BY rating DESC LIMIT 1")
                movie = cur.fetchone()[0]
                cur.close()

                message = f"Happy Birthday {name}! The top rated movie from your birth year ({dob.year}) is {movie}. Click this link to send birthday wishes on Whatsapp: https://wa.me/{phone}?text=Happy%20Birthday%20{name}!"
                channel = client.get_channel(1096374826865791058) 
                await channel.send(message)

@client.event
async def on_ready():
    send_birthday_wishes.start()
    print('Bot is ready.')

client.run('MTA5NjM3MTg0NzUwMDY3MzA1Ng.GmE2iW.eXYDD52ULS4HBa9eLvwU7ynmBx4_KFyQmYPHyA')
