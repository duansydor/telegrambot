import telebot
import random
import requests as req
import json
CHAVE_API = "5362564731:AAE9lQDU_AK36kPBhxZgAh9QJYgGpiU7QEY"
ANIME_API = "https://api.jikan.moe/v4/anime/{}"
bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao1"])
def searchHentai(mensagem):
  numbers = []
  for i in range(5):
    randnum =random.randrange(1,10)
    numbers.append("{}".format(randnum))
  sauce = "".join(numbers)
  bot.reply_to(mensagem,"hentaizao \n https://nhentai.net/g/{}".format(sauce))
  
@bot.message_handler(commands=["opcao2"])
def sugerirAnime(mensagem):
  numbers = []
  for i in range(3):
    randnum =random.randrange(1,9)
    numbers.append("{}".format(randnum))
  sauce = "".join(numbers)
  jsonData = req.get(ANIME_API.format(sauce))
  anime = json.loads(jsonData.text)
  
  if "status" in anime:
    bot.reply_to(mensagem,"tente novamente: {}".format(sauce))
  else:
    bot.reply_to(mensagem, "Titulo: {} \n Sinopse: {} \n /menu - voltar para o menu".format(anime["data"]["title"], anime["data"]["synopsis"]))
  
  
#mensagem padrao
def verificar(mensagem):
    return True
@bot.message_handler(func=verificar, commands=["start","menu"])
def responder(mensagem):
  bot.reply_to(mensagem, """
  Escolha uma opçao
  /opcao1 - gerar link de hentai
  /opcao2 - Sugestao de anime
  """)

bot.polling()