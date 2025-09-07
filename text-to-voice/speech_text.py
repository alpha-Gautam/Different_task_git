import pyttsx3
import time
import google.generativeai as genai

# Configure your API key
# Replace "YOUR_API_KEY" with your actual API key
genai.configure(api_key="AIzaSyCTcndwqmw65Xonykm9twax1VlsbpFNAd8") 

# For a synchronous call (most common for simple requests)
model = genai.GenerativeModel('gemini-2.5-flash') # Using 'gemini-pro' as 'gemini-2.5-flash' might be a future or internal model name
response = model.generate_content("discribe in 5 lines,use professional words:-" + "tell some interesting about google")
txt= response.text
print(txt)


# # If you were working with streaming responses (for longer outputs)
# response_stream = model.generate_content("discribe in 5 lines,use professional words"+"tell some interesting about google", stream=True)
# for chunk in response_stream:
#     print(chunk.text)
#     time.sleep(1)




def tell(txt:str,speed=100):
    engine = pyttsx3.init()
    if speed:
        engine.setProperty('rate', value=speed)
    engine.say(txt)
    engine.runAndWait()
    engine.stop()

def speech(txt:str):
    tell("starting the speech")
    # tell(txt)
    for i in txt.split(" "):
        n=len(i)
        slp=max(0,n*0.01)
        print(i," ")
        tell(i)
        time.sleep(slp)

# speech(txt)