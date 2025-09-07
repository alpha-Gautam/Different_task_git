import gtts
import playsound

# # text = input("Enter some text here:- ")

# text='''To learn Python Programming online with regular LIVE CLASSES, enroll now: https://bit.ly/python-course-wscube-tech

# 👉Check Out the Course Module: https://drive.google.com/file/d/1UI6_...
 
# '''

# file_name=""

# with open("cp-1.txt","r") as f:
#     data=f.read()

# print(data)


'''
to change the accents 

"en" for english,
"hi" for hindi,
"fr" for french,
'''

data="this is a test file for gtts"

sound = gtts.gTTS(str(data), lang="en")

# sound.save("chaper-1.mp3")

# playsound.playsound("textsound.mp3")
# playsound.playsound(sound)

from platform import system
system = system()

print("System is: ", system)
