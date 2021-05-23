from snowballstemmer import TurkishStemmer
import speech_recognition as sr
import webbrowser
from time import ctime
import commands
import datetime
import requests
import time
import os
import pyttsx3
import random
import feedparser







class questions:
    baba = [
        "Benim Babamın adı Uğurcan KUZU",
        "Teknik olarak Babam yok fakat benim oluşmamda önemli payı olan Uğurcan'ı babam olarak kabul edebiliriz."

    ]
class salute:
    saluteMorning = [
        "Merhaba Patron, Günün umarım güzel geçer !",
        "Selam Patron, Kahveni içtin mi ?"
    ]
    saluteNoon = [
        "Selam Patron, bir şeyler yapmak için oldukça uygun bir zaman gibi ",
        "Naber Patron, e-postalarını kontrol etmeyi unutma"

    ]
    saluteEvening = [
        "İyi akşamlar patron, Yorucu bir gün müydü ?",
        "İyi Akşamlar Patron, Umarım çok yorgun değilsindir. "
    ]
class şarkı:
    şarkılar = [
        "https://www.youtube.com/watch?v=etAIpkdhU9Q&ab_channel=acdcVEVO",
        "https://www.youtube.com/watch?v=o1tj2zJ2Wvg&ab_channel=GunsNRosesVEVO",
    ]
class uygulamalar:
    uygulama_listesi = ["Spotify.app","Discord.app","Pages.app","Steam.app"]
