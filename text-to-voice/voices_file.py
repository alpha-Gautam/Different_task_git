import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

print(f"Your system has {len(voices)} voices installed:\n")

for i, voice in enumerate(voices):
    print(f"Voice {i}:")
    print(f" - ID   : {voice.id}")
    print(f" - Name : {voice.name}")
    print(f" - Lang : {voice.languages}")
    print(f" - Gender (if available): {getattr(voice, 'gender', 'Unknown')}")
    print()
