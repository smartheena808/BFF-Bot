import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

# helping function
def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]

  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements  

# create discord object called client
client = discord.Client()

# list of sad words
sad_words = ["sad","unhappy", "stress", "depressing", "depressed", "angry", "lost motivation"]

# list of encourange words
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You're a great person!",
  "Be Happy!"
  ]

# get quote from zenquote.io api
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")

  json_data = json.loads(response.text)

  quote = json_data[0]['q'] + " - " + json_data[0]['a']

  return (quote)

# Message that Bot is up and running
@client.event
async def on_ready():
  options = starter_encouragements
  if "encouragements" in db.keys():
    options = options + db["encouragements"]
  print(f'We have logged in as {client.user}')


# Bot reply message
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  words = message.content

  if words.startswith('hello'):
    await message.channel.send('Hi there.')

  if words.startswith('inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in words for word in sad_words):
    await message.channel.send(random.choice(db["encouragements"]))

# adding new encouragement messages
  if words.startswith("AEM:"):
    encouraging_message = words.split('AEM: ',1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send('New encourage message added.')

  if words.startswith("Remove"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(words.split('Remove ',1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)  

  if words.startswith('Show list'):
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
      await message.channel.send(encouragements)

# run the Bot
keep_alive()
client.run(os.getenv('TOKEN'))



