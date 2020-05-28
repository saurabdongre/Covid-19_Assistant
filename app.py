from chatbot import chatbot
from flask import Flask, render_template, request
import random
import re
import webbrowser
import smtplib
import os

trainer_dict = []

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText != 'exit':
        trainer_dict.append(userText)
        reply_text = str(chatbot.get_response(userText))
        trainer_dict.append(reply_text)
        return reply_text
    else:
        writeFile()
        return "Goodbye"
        os.exit(0)

def sendEmail(body):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("user", "pass")

    SUBJECT = "Incident Creation"
    TEXT = "Dummy Text"
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    server.sendmail("user@gmail.com", "user@gmail.com", msg)
    server.quit()


def writeFile():
    from datetime import datetime
    #filename = '\training_data\'+datetime.now().strftime("%d%m%Y%I%M%S%p")+".txt"
    #filename = r"\training_data"+r'\'+datetime.now().strftime("%d%m%Y%I%M%S%p")+".txt"
    
    dir = os.path.dirname(os.path.abspath(__file__))
    filename = datetime.now().strftime("%d%m%Y%I%M%S%p")+".txt"
    rel_path = "training_data\\"+filename
    path = os.path.join(dir, rel_path)
    with open(path, 'w+') as f:
        for item in trainer_dict:
            f.write("%s\n" % item)
        
        
    #path1 = '\training_data\' + str(filename)
    #path = path1 + '.txt'
    #if 'summary:' in text.lower(): 
    #    f= open("\training_data\"+filename+".txt","w+")
    #else:   
    #    f= open("\dummy.txt","a+")
    #f.write(text+"\n")

if __name__ == "__main__":
    webbrowser.open('http://localhost:5000')
    app.run()
