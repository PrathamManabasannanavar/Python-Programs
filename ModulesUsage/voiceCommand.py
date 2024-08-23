import speech_recognition as sr
import subprocess;
import pyttsx3;

def textToAudio(text):
    engine = pyttsx3.init();
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text);
    engine.runAndWait();

def voiceCommand():
    # Initialize the recognizer
    recog = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print('Listening...')
        
        # Adjust for ambient noise and record audio
        recog.adjust_for_ambient_noise(source)
        audio = recog.listen(source)
        
        # Optionally, you might want to add code to process the audio, e.g., recognize speech
        try:
            text = recog.recognize_google(audio)
            print("You said:", text)
            if(text.lower() == "open chrome"):
                textToAudio("Opening Chrome")
                subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe");
            elif(text.lower() == "open brave"):
                textToAudio("Opening Brave")
                subprocess.Popen("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe");
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


textToAudio("Hello this is Jarvis AI, built by Pratham")
while(True):
    voiceCommand()
