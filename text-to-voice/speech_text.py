import pyttsx3
import random
# engine = pyttsx3.init()
# engine.say("Hello, this is a test.")
# engine.runAndWait()
def tell(txt:str,speed=None):
    engine = pyttsx3.init()
    if speed:
        engine.setProperty("rate",speed)
        word_rate=engine.getProperty("rate")
        # word_rate=speed
        print("word_rate: ",word_rate)
    engine.say(txt,)
    engine.runAndWait()
    

# pyttsx3.getProperty("")
data="this is the test i know but you need to utilize all the resources for get a best result"
for i in data.split(" "):
    
    tell(i,speed=random.randint(50,200))
    # engine = pyttsx3.init()
    # engine.say(i)
    # engine.runAndWait()
    
    
    
    
    
    # pyttsx3.speak(i)