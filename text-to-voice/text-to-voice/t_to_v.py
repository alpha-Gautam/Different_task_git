import gtts
import playsound

# text = input("Enter some text here:- ")

text='''To learn Python Programming online with regular LIVE CLASSES, enroll now: https://bit.ly/python-course-wscube-tech

👉Check Out the Course Module: https://drive.google.com/file/d/1UI6_...
 
'''






'''
to change the accents 

"en" for english,
"hi" for hindi,
"fr" for french,
'''

sound = gtts.gTTS(text, lang="en")



sound.save("textsound.mp3")

playsound.playsound("textsound.mp3")