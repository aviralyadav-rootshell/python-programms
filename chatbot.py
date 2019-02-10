from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os

chatbot = ChatBot(
    'Tron',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='./chatdatabase.sqlite3'
)

chatbot.set_trainer(ListTrainer)

for files in os.listdir('/home/tron/python box/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open('/home/tron/python box/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    chatbot.train(data)



while True:
    query = input("You:")
    response=chatbot.get_response(query)
    print("Tron : ",response)
