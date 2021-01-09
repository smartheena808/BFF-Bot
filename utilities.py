from replit import db
import requests
import json

class BotUtilities():
  """
    Contains helping functions to make a BFF_Bot runs as a best friend, such as generate encouragement message.
  """

  sad_words = []

  def __init__(self):
    sad_words = self.get_sadwords()
    if len(sad_words) == 0:
      self.create_sadwords()

  def create_sadwords(self):
    """ Create a list of sad words from the starter that user can add more       later. 
    """
    starter_sadwords = [
      "sad","unhappy", "stress", "depressing", "depressed", "angry", "lost motivation", "desperate", "heavy heart", "dejected", "frustrated", "crusted", "disgusted", "upset", "hateful", "sorrowful", "mournful", "weepy", "alone", "burdened", "devastated", "disappointed", "discouraged", "gloomy", "hopeless", "let down", "lonely", "heartbroken", "miserable", "neglected", "pessimistic", "solemn", "resentful"
      ]

    for word in starter_sadwords:
      if "sadwords" in db.keys():
        sad_words = db["sadwords"]
        if word not in sad_words:
          sad_words.append(word)
          db["sadwords"] = sad_words
        else:
          pass
      else:
        db["sadwords"] = [word]        
  
  def update_sad_keywords(self, word):
    """ Function to add more keywords for sad emotions to the database
        ::param: string word
    """
    if "sadwords" in db.keys():
      sad_words = db["sadwords"]
      if word not in sad_words:
        sad_words.append(word)
      db["sadwords"] = sad_words
    else:
      db["sadwords"] = [word]

  def delete_sadword(self, index):
    """ Function to delete keyword of sad emotion from the database
        ::param: int index (position of the keyword in database)  
    """
    sad_words = db["sadwords"]

    if len(sad_words) > 0 and len(sad_words) > index:
      del sad_words[index]
    db["sadwords"] = sad_words

  def get_sadwords(self):
    """ Get all the sad emotion keyword that are stored in database. 
        ::return: a list of sad words from database
    """
    if "sadwords" not in db.keys():
      db["sadwords"] = []
    return db["sadwords"]

  def isSadWord(self, word):
    """ Checking whether a given word is a sad emotion keywords
        ::param: string word 
        ::return: boolean of isSadWord 
    """
    sad_words = self.get_sadwords()
    isWordSad = False
    if word in sad_words:
      isWordSad = True 
    return isWordSad

  def create_encouragements(self):
    """ Create a collection of encourage words in database that can added        later. 
    """
    encouragements = []
    starter_encouragements = [
    "Cheer up!","Hang in there.","You're a great person!","Be Happy!"
    ]
    for encouragement in starter_encouragements:
      if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        if encouragement not in encouragements:
          encouragements.append(encouragement)
          db["encouragements"]= encouragements
        else:
          pass  
      else:
        db["encouragements"] = [encouragement] 

  def get_encouragements(self):
    """ Get the encouragement words from database
        ::return: a list of encouragement words 
    """
    if "encouragements" not in db.keys():
      db["encouragements"] = []
    return db["encouragements"]

  def update_encouragements(self, encouraging_message):
    """ Adding a new encouragement words to database if it does not exists       in the database.
        ::param: string encouraging_message 
    """
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
      if encouraging_message not in encouragements:
        encouragements.append(encouraging_message)
      db["encouragements"] = encouragements
    else:
      db["encouragements"] = [encouraging_message]

  def delete_encouragement(self,index):
    """ Delete a encouragement words in the database.
        ::param: int index (position of the encouragement words) 
    """
    encouragements = db["encouragements"]

    if len(encouragements) > 0 and len(encouragements) > index:
      del encouragements[index]
    db["encouragements"] = encouragements  

  # get quote from zenquote.io api
  def get_quote(self):
    """ Get a new quote alive from zen quote API randomly.
        ::return: string quote 
    """
    response = requests.get("https://zenquotes.io/api/random")

    json_data = json.loads(response.text)

    quote = json_data[0]['q'] + " - " + json_data[0]['a']

    return (quote)
