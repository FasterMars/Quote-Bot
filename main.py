from keep_alive import keep_alive
import os
import discord
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0] ['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('$quote'))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote)

  # Replies to swears

  if message.content.startswith('fuck'):
    await message.channel.send('No swearing!')
  
  if message.content.startswith('Fuck'):
    await message.channel.send('No swearing!')
  
  if message.content.startswith('bitch'):
    await message.channel.send('No swearing!')

  if message.content.startswith('Bitch'):
    await message.channel.send('No swearing!')

  if message.content.startswith('saale'):
    await message.channel.send('No swearing!')

  if message.content.startswith('F off'):
    await message.channel.send('No swearing!')

  if message.content.startswith('Chutiye'):
    await message.channel.send('No swearing!')

  if message.content.startswith('chutiye'):
    await message.channel.send('No swearing!')

  if message.content.startswith('f u c k'):
    await message.channel.send('No swearing!')

  if message.content.startswith('fuck'):
    await message.channel.send('No swearing!')

  # Replies to hello, hi, etc...
  
  if message.content.startswith('helo'):
    await message.channel.send('Hi There!')

  if message.content.startswith('hola'):
    await message.channel.send('Hola amigão!')

  if message.content.startswith('bonjour'):
    await message.channel.send('Bonjour Monsieur!')

  if message.content.startswith('konichiwa'):
    await message.channel.send('Konichiwa!')

  if message.content.startswith('Hola'):
    await message.channel.send('Hola amigão!')

  if message.content.startswith('Bonjour'):
    await message.channel.send('Bonjour Monsieur!')

  if message.content.startswith('Konichiwa'):
    await message.channel.send('Konichiwa!')

  if message.content.startswith('hi'):
    await message.channel.send('Hi There!')

  if message.content.startswith('Hi'):
    await message.channel.send('Hi There!')

  if message.content.startswith('hello'):
    await message.channel.send('Hi There!')
  
  if message.content.startswith('Hello'):
    await message.channel.send('Hi There!')
  
  if message.content.startswith('how are you?'):
    await message.channel.send('I am fine!, how are you?')

  # Replies to Bye, etc.

  if message.content.startswith('bye'):
    await message.channel.send('Bye! Have a good day!')

  if message.content.startswith('Bye'):
    await message.channel.send('Bye! Have a good day!')
    
  # Responses to ' How are you? '

  if message.content.startswith('I am good'):
    await message.channel.send(':smile:')

  if message.content.startswith('im fine'):
    await message.channel.send(':smile')
  
  if message.content.startswith('Im good'):
    await message.channel.send(':smile:')

  if message.content.startswith('i am fine'):
    await message.channel.send(':smile:')

  if message.content.startswith('i am good'):
    await message.channel.send(':smile:')

  # Replies to greetings

  if message.content.startswith('GM'):
    await message.channel.send('Good Morning! Have a nice day.')

  if message.content.startswith('gm'):
    await message.channel.send('Good Morning! Have a nice day.')

  if message.content.startswith('Good morning'):
    await message.channel.send('Good Morning! Have a nice day.')

  if message.content.startswith('good morning'):
    await message.channel.send('Good Morning! Have a nice day.')

keep_alive()

client.run('OTM3OTQzODMzMzk4ODg2NDEw.YfjGRA.gND2V3wiae8hNanCq_4qD8H1p5o')
