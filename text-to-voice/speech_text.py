import pyttsx3
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()


# Replace "YOUR_API_KEY" with your actual Google  API key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 

# # For a synchronous call (most common for simple requests)
# model = genai.GenerativeModel('gemini-2.5-flash') # Using 'gemini-pro' as 'gemini-2.5-flash' might be a future or internal model name\
# topic="Space "
# response = model.generate_content(f"give latest and interesting information about the topic in 5 lines and use professional words:\n topic:-{topic}" )
# txt= response.text
# print(txt)

class Dictation:
    speed=125
    topic="anyone like('history', 'future', 'economy',' mathematics', 'physics')"

    pause_constant=25
    

    def __init__(self):
        
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        
    def text_generate(self):
        try:
            response = self.model.generate_content(f"give formal information about the topic in 50 words and use professional words on topic {self.topic}" )
            text= response.text
            print(text)
            # self.speech(txt)
            return text
        except:
            text='Dictation is the transcription of spoken text: one person who is "dictating" speaks and another who is "taking dictation" writes down the words as they are spoken. Among speakers of several languages, dictation is used as a test of language skill, similar to spelling bees in the English-speaking world.'
            print(text)
            return text

    def tell(self, txt:str, speed=speed):
        engine = pyttsx3.init()
        if speed:
            engine.setProperty('rate', value=speed)
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
        if a=='q':
	        break

		

