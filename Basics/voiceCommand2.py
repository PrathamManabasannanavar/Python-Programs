import speech_recognition as sr
import subprocess;
import pyttsx3;
import psutil;
import sys;

processes = []

class Application:
    pid = None
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def createProcess(self):
        self.pid = subprocess.Popen(self.path).pid
        processes.append(self)

    @staticmethod
    def removeProcess(processName):
        for process in processes:
            if(process.name.lower() == processName.lower()):
                try:
                    process.wait(timeout=5) #wait childprocess --> ends
                except:    
                    psutil.Process(process.pid).terminate()
                processes.remove(process)
                return
            
                

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
            if text.lower() == "exit" or text.lower() == 'jarvis exit':
                textToAudio("Exited");
                sys.exit(0)
            elif(text.lower() == "open chrome"):
                textToAudio("Opening Chrome")
                Application("chrome", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe").createProcess();
            elif(text.lower() == "open brave"):
                textToAudio("Opening Brave")
                Application("brave", "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe").createProcess();

            elif(text.lower() == "close chrome"):
                textToAudio("Closing Chrome")
                Application.removeProcess("chrome")
            elif(text.lower() == "close brave"):
                textToAudio("Closing Brave")
                Application.removeProcess("brave")

        except sr.UnknownValueError:
            print("Sorry, could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

# start of the execution

textToAudio("Hello I am Jarvis, voice command please")

while(True):
    voiceCommand()
