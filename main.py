import discord
import os
import random
from keep_alive import keep_alive
from utilities import BotUtilities

# create discord object called client
client = discord.Client()
bot = BotUtilities() 
encouragements = []

# initial message that Bot is up and running
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

# Bot reply the message
@client.event
async def on_message(message):
  # populate the data from database 
  encouragements = bot.get_encouragements()
  if len(encouragements) == 0:
    bot.create_encouragements()

  sentence = message.content
  list_words = sentence.split(' ')

# don't reply the message if from the bot
  if message.author == client.user:
    return

  if sentence.startswith('hello'):
    await message.channel.send('Hi there.')

  if sentence.startswith('Inspire'):
    quote = bot.get_quote()
    await message.channel.send(quote)

  if not(sentence.startswith('Show sadwords list')):
    for word in list_words:
      if bot.isSadWord(word):
        await message.channel.send(random.choice(encouragements))
        break

# adding new encouragement messages
  if sentence.startswith("Add encouragement: "):
    encouraging_message = sentence.split('Add encouragement: ',1)[1]
    bot.update_encouragements(encouraging_message)
    await message.channel.send('New encourage message added.')

# removing encouragements list using index number
  if sentence.startswith("Remove encouragement"):
    encouragements = []
    index = int(sentence.split('Remove encouragement ',1)[1])
    bot.delete_encouragement(index)
    encouragements = bot.get_encouragements()
    await message.channel.send(encouragements)  

# showing encouragements words 
  if sentence.startswith('Show encouragement list'):
    encouragements = bot.get_encouragements()
    await message.channel.send(encouragements)

# adding new sad words
  if sentence.startswith("Add sadwords: "):
    sad_words = sentence.split('Add sadwords: ',1)[1]
    bot.update_sad_keywords(sad_words)
    await message.channel.send('New sad words added.')

# removing sad words list using index number
  if sentence.startswith("Remove sadwords"):
    sad_words = []
    index = int(sentence.split('Remove sadwords ',1)[1])
    bot.delete_sadword(index)
    sad_words = bot.get_sadwords()
    await message.channel.send(sad_words)  

# showing sad words list 
  if sentence.startswith('Show sadwords list'):
    sad_words = bot.get_sadwords()
    await message.channel.send(sad_words)


# run the Bot
keep_alive()
client.run(os.getenv('TOKEN'))



