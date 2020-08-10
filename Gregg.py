import speech_recognition as sr
import json
import webbrowser

class Gregg:

    def __init__(self):
        self.recognizer = sr.Recognizer()

        with open("SECURE/G-API-Creds.json") as file:
            credsDict = json.load(file)
            self.GOOGLE_API_CREDENTIALS = json.dumps(credsDict)
            file.close()

    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source, None, 5)
            print("Finished")

        try:
            speech = self.recognizer.recognize_google_cloud(audio, self.GOOGLE_API_CREDENTIALS)
        except sr.UnknownValueError:
            print("Google cloud speech could not understand the audio.")
        except sr.RequestError as e:
            print("Google Cloud Speech was unreachable: {0}".format(e))

        self.parseForCommand(speech)

    def parseForCommand(self, speech):

        command = speech[:speech.find(" ")]

        if command == "Google":
            self.google(speech[speech.find(" ") + 1:])


    def google(self, query):
        webbrowser.open_new_tab("https://www.google.com/search?q=" + query)





# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say Something!")
#     audio = r.listen(source)
#     print("Got It!")
#
# with open("SECURE/G-API-Creds.json") as file:
#     credsDict = json.load(file)
#     GOOGLE_API_CREDENTIALS = json.dumps(credsDict)
#     file.close()
#
# speech = ""
#
# try:
#     speech = r.recognize_google_cloud(audio, GOOGLE_API_CREDENTIALS)
# except sr.UnknownValueError:
#     print("Google cloud speech could not understand the audio.")
# except sr.RequestError as e:
#     print("Google Cloud Speech was unreachable: {0}".format(e))
#
# print(f"You said: {speech}")
