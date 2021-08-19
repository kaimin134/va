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

def main():
    you = nghe()
    if "yes" in you or "yeah" in you or "yup" in you or "ok" in you:
        brain = "You wanna get Vietnamese, Korean or Japanese food?"
        noi(brain)
        you = nghe()
        if "Vietnamese" in you:
            brain = "okay, and you wanna food with soup or nah?"
            noi(brain)
            you = nghe()
            if "yes" in you or "yeah" in you or "yup" in you or "ok" in you or "with" in you:
                brain = "nice! you could try fer, boom bor, boom real, who tew. Hope you will enjoy. Good bye!"
            elif "no" in you or "nah" in you or "don't" in you or "nope" in you:
                brain = "okay, you could try com thit nuong, com gha, banh mi, fo af chao. Hope you will enjoy it. Good bye!"
            else:
                brain = "sorry, I didn't get that. Please start again"
            noi(brain)
        elif "Korean" in you:
            brain = "You could try Korean BBQ, Shabu-Shabu. Hope you will enjoy it. Good bye!"
            noi(brain)
        elif "Japanese" in you:
            brain = "You could try sushi, ramen noodles, udon noodles. Hope you will enjoy it. Good bye!"
            noi(brain)
        else:
            brain = "sorry, I don't understand. Please start again"
            noi(brain)
    elif "no" in you or "nah" in you or "don't" in you or "nope" in you:
        brain = "How you think about fast food?"
        noi(brain)
        you = nghe()
        if "yes" in you or "yeah" in you or "yup" in you or "ok" in you:
            brain = "there are some good choices for you: fried chicken, burgers, sandwiches, hot dog, tacos, burritos. Hope you will enjoy it. Good bye!"

            noi(brain)
        elif "no" in you or "nah" in you or "don't" in you or "nope" in you:
            brain = "you could go to get steak or chicken wings"
            noi(brain)
    else:
        brain = "sorry, I don't understand. Please start again "
        noi(brain)
greeting = ""
import datetime
currentTime = datetime.datetime.now()
currentTime.hour
0
if currentTime.hour < 12:
    greeting = "Good morning."
elif 12 <= currentTime.hour < 18:
    greeting = "Good afternoon."
else:
    greeting = "Good evening."

brain = greeting + " I will recommend you some food. Please give me some hints. Do you want Asian food?"

noi(brain)
main()