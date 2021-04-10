import pyglet
import speech_recognition as sr
from commands import Commander


r = sr.Recognizer()
cmd = Commander()
running = True


# noinspection PyBroadException
def initSpeech():
    print("Listening...")
    file = pyglet.resource.media('Audio/pristine-609.mp3')
    file.play()

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    file1 = pyglet.resource.media('Audio/swiftly-610.mp3')
    file1.play()

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you, bro.")

    print("Your Command:")
    print(command)
    if command in ["quit", "exit", "bye", "goodbye"]:
        global running
        running = False

    cmd.discover(command)


while running:
    initSpeech()
