def nghe():
    import speech_recognition
    robot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("iMinh: I'm Listening")
        audio = robot_ear.listen(mic, timeout=3, phrase_time_limit=3)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)
    return you

def noi(name):
    import pyttsx3
    print("iMinh: " + name)
    mouth = pyttsx3.init()
    mouth.say(name)
    mouth.runAndWait()
import random

food = ["fer", "boom bor", "boom real", "who tew", "com thit nuong", "com gha", "banh mi", "fo af chao", "Korean BBQ", "Shabu-Shabu", "sushi", "ramen noodles", "udon noodles", "fried chicken", "burgers", "sandwiches", "hot dog", "tacos", "burritos", "steak", "chicken wings"]
you = ""
while "yes" not in you:
    noi("I pick " + random.choice(food) + " for you. Are you okay with that?")
    you = nghe()

noi("okay, let's go to get that")