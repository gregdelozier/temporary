from win32com.client import Dispatch

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

if __name__=='__main__':
    with open(all_languages.txt) as f:
        for item in f.readlines():
            speak(item)