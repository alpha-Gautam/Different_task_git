import pyttsx3
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
import datetime
import random


class Dictation:
    speed=125

    topic="anyone like ('history', 'future', 'economy','mathematics', 'physics', 'philosophy', 'science', 'technology', 'biology', 'chemistry', 'geography', 'politics')"

    pause_constant=25
    
    def __init__(self):
        
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        
    def text_generate(self):
        try:
            # Generate random datetime
            random_year = random.randint(1900, 2100)
            random_month = random.randint(1, 12)
            random_day = random.randint(1, 28)
            random_hour = random.randint(0, 23)
            random_minute = random.randint(0, 59)
            random_second = random.randint(0, 59)
            random_datetime = datetime.datetime(random_year, random_month, random_day, random_hour, random_minute, random_second)
            # Updated prompt to request a new paragraph each time, even for the same topic
            response = self.model.generate_content(f"Write a paragraph about the any of the topic in 50 words using professional words according to time {random_datetime.isoformat()}" )
            
            
            text= response.text
            print(text)
            # self.speech(txt)
            return text
        except:
            text='Dictation is the transcription of spoken text: one person who is "dictating" speaks and another who is "taking dictation" writes down the words as they are spoken. Among speakers of several languages, dictation is used as a test of language skill, similar to spelling bees in the English-speaking world.'
            print(text)
            return text

    def tell(self, txt: str, speed=None, voice_id=0):
        if speed is None:
            speed = Dictation.speed
        engine = pyttsx3.init()
        if speed:
            engine.setProperty('rate', value=speed)
        if voice_id:
            voices = engine.getProperty('voices')
            if voice_id < len(voices):
                engine.setProperty('voice', voices[voice_id].id)
        engine.say(txt)
        engine.runAndWait()
        engine.stop()

    def speech(self):
        txt=self.text_generate()
        self.tell("starting the speech")
        pause_time=self.pause_constant/100
        for i in txt.split(" "):
            sleep_time=pause_time*len(i)
            # slp=max(0,n*0.05)
            print(i," ")
            self.tell(i)
            time.sleep(sleep_time)

        time.sleep(1)
        self.tell("Now speech is ended! Thank you for listening")
    @classmethod
    def update_pause_constant(cls, new_speed:int):
        cls.pause_constant=new_speed
        print(f"Speed updated to {cls.pause_constant} words per minute")


if __name__=="__main__":
    d=Dictation()
    d.speech()
    while(True):
        a=input('Enter q to quit: \n')
        if a=='s':
            d.speech()
        if a=='q':
            break



