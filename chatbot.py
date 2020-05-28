from chatterbot import ChatBot

chatbot = ChatBot(
    'ChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        #'chatterbot.logic.MathematicalEvaluation',
        #'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.95
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
from chatterbot.trainers import ListTrainer
trainer = ListTrainer(chatbot)

#training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
#training_data_personal = open('training_data/personal_ques.txt').read().splitlines()
#training_data = training_data_quesans + training_data_personal

import glob
files=[]
files = glob.glob("training_data/*.*")
print(files)
print(type(files))
training_data=[]
for f in files:
    data_SDO = open(f).read().splitlines()
    #print(data_SDO)
    #print(type(data_SDO))
    training_data = training_data + data_SDO

trainer.train(training_data)

# Training With Corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer_corpus = ChatterBotCorpusTrainer(chatbot)

trainer_corpus.train(
    'chatterbot.corpus.english'
)
