import speech_recognition as sr
import webbrowser as wb
import commands.__init__
from time import ctime
import datetime
import requests
import time
import os
import pyttsx3
import random
import smtplib
import feedparser
from snowballstemmer import TurkishStemmer

def mail(mail,alıcı):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.connect('smtp.gmail.com',465)
    server.command_encoding = 'utf-8'
    server.login("<Mail>","<Password>")
    server.sendmail(from_addr='ugurcankzuit@gmail.com',to_addrs=alıcı,msg=mail.encode('utf8'))
    server.quit()
    konuş("Gönderildi Patron !")
def haberler():
    konuş("Bulabildiğim haberler şunlar patron:")
    feed_cont = requests.get('https://feeds.bbci.co.uk/turkce/rss.xml')
    feed = feedparser.parse(feed_cont.text)
    entry = feed.entries
    for i in range(0,3):
        konuş(entry[i].summary)

    konuş("Başka bir isteğin var mı patron ? ")
def questions(soru):
    if(all(i in soru for i in ["baba","kim"])):
        konuş(random.choice(commands.questions.baba))
    else:
        pass

def music():
    konuş("Yolluyorum Patron")
    wb.open(random.choice(commands.şarkı.şarkılar))
def durdurma(data):
    while True:
        if(any(i in data for i in ["dur","yeter","yeterli","kapat","kapatabilir"])):
            return False
            break
        else:
            return True
            break



#############################################
def kökBulma(list):
    stemmer = TurkishStemmer()
    return stemmer.stemWords(list)
def konuş(audioString):
    engine = pyttsx3.init()
    engine.setProperty('rate',178)
    engine.say(audioString)
    engine.runAndWait()
def dinle():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Dinliyorum:')
        r.pause_threshold = 1
        audio = r.listen(source)
        data = ""
        try:
            data = r.recognize_google(audio,language='tr-tr')
            print("{}".format(data))

        except:
            print("Başarısız")
        return data
def asistan(data):
    a = kökBulma(data.lower().split())
    print(a)
    if(any(i in a for i in ["merhap","sela"])):#Selam Verme Fonksiyonu
        try:
            if(datetime.datetime.now().hour >=0 and datetime.datetime.now().hour<=12):
                konuş(random.choice(commands.salute.saluteMorning))
            elif(datetime.datetime.now().hour >=12 and datetime.datetime.now().hour<=18):
                konuş(random.choice(commands.salute.saluteNoon))
            else:
                konuş(random.choice(commands.salute.saluteEvening))
        except:
            asistan(data)

    elif(any(i in a for i in["şarkı","müzik"]) and "aç" in a):#Müzik Fonksiyonu
        music()
        konuş("Başka bir isteğin var mı patron ?")

    elif(all(i in a for i in ["haber","ne"])):#Haber Okuma Fonksiyonu
        haberler()
    elif(all(i in a for i in ["sor","sormak"])):#Soru Sorma Fonksiyonu
        konuş("Tabii ki patron, ne istersen...")
        while True :
            data = kökBulma(dinle().lower().split())
            questions(data)
            x=durdurma(data)
            print(x)
            if (x != True):
                konuş("Yardımcı olduysam ne mutlu... Başka ne istersin patron ?")
                break
            else:
                konuş("Başka ne öğrenmek istersin patron ?")
                continue
    elif(any(i in a for i in["mail","epos"]) and any(j in a for j in ["yollamak","yol","at","atmak","gönder"])):
        konuş("Tabii ki patron. Kime Yollamak istediğinizi bana yazar mısınız ?")
        alıcı = input()
        print(alıcı)
        konuş("Neyi iletmemi istersiniz ? ")
        mesaj = dinle()
        konuş("Yolluyorum patron")
        mail(mesaj,alıcı)




##################################################################
konuş("Konuşma modülü aktif...\nSes - Yazı Dönüşümü Aktif...\n Fonksiyonlar aktif...\n  Ben Valeria, Hizmete hazırım ")
while True:
    asistan(dinle())

