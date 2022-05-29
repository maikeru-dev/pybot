#!/usr/bin/env python3
import sys
from venv import create
import discord, discord.ext
import sqlite3
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

## Discord:

class Bot(discord.Client):
  # Connecting...
  async def on_connect(self):
    print('Connected to Discord.')
    return

  async def on_ready(self):
    print('Ready.')
    # Terminal commands:
    while(cli):
      x = input('>')
      if x == 'close':
        print('Shutting down.')
        exit()
      if x == 'read':
        viewAllRows()
      else:
        print('Unknown command. Known(close, read).')

  # Processing...
  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith(symbol):
      print(message.content)
      return

  async def on_voice_state_update(self, member, before, after):
    id = member.id
    if after.channel != None:
      #Left the channel
      print('Left the channel.')
      return

    elif before.channel == None & after.channel != None:
      #Joined the channel
      print('Joined the channel.')
      return

## SQL:

def viewAllRows():
  conn = sqlite3.connect('test.db')
  cur = conn.cursor()

  for row in cur.execute('SELECT * FROM userdata ORDER BY time'):
    print(row)

  conn.close()

def createTables():
  conn = sqlite3.connect('test.db')

  conn.execute('''CREATE TABLE userdata
              (
                id INTEGER NOT NULL, 
                serverId INTEGER NOT NULL,
                time INTEGER,
                PRIMARY KEY (id, serverId)
                );
  ''')

  conn.execute('''CREATE TABLE serverdata
              (
                serverId INTEGER NOT NULL,
                PRIMARY KEY (serverId)
              )''')

  conn.close()


## Execution:

#Config
key = sys.argv.pop()
cli = False
symbol = '.'
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

viewAllRows()


client = Bot(intents=intents)
client.run(key)