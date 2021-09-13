import requests
from bs4 import BeautifulSoup
import random
import scrape
from twilio.rest import Client
from config import config

scrape.scrape()
client = Client(config['TWILIO_ACCOUNT_SID'], config['TWILIO_AUTH_TOKEN'])
with open('word.txt',encoding='utf-8') as file:
    message = file.read()

message = client.messages.create(to = config['MY_NUMBER'], 
  from_ = config['MY_TWILIO_NUMBER'],
  body = message
)