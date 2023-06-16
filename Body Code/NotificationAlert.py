import os
import shutil
from sys import argv
import pyttsx3
from time import sleep
import threading

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',185)

def autoVolumeIncreaser(volume=25):
    from pynput.keyboard import Key, Controller
    keyboard = Controller()

    for i in range(volume):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def Notification(title, message, app_name, toast, timeout):
    from plyer import notification
    notification.notify(
        title=title,
        message=message,
        app_name=app_name,
        toast=toast,
        # displaying time
        timeout=timeout,

    )


def selfDestruction(timer=0):
    sleep(timer)
    os.remove(argv[0])


def coreExistenceDelete():
    if len(os.listdir("StockAverage")) != 0:
        os.chdir("StockAverage")
        shutil.rmtree(os.getcwd(), ignore_errors=True)

        # Now we are getting out of StockAverage Directory to Desktop and then deleting the Directory
        path1 = os.path.normpath(os.getcwd())

        path1 = list(path1.split(os.sep))

        path1.pop(-1)  # To get out of 'StockAverage' Directory

        path1 = "/".join(path1)

        os.chdir(path1)
        # Now we are in Desktop

        os.rmdir("StockAverage")

    else:
        os.rmdir("StockAverage")


# mainThread1= threading.Thread(target=autoVolumeIncreaser(26))
# mainThread2 = threading.Thread(target=Notification("StockAverage Alert",
#                                                    "Owner of StockAverage has removed now their code from your Computer for some "
#                                                    "Security Purposes and rights", "StockAverage", True, 7))
# mainThread3 = threading.Thread(target=speak("Now I am Self Destructing Myself"))
mainThread4 = threading.Thread(target=coreExistenceDelete)

# mainThread1.start()
# mainThread2.start()
# mainThread3.start()
mainThread4.start()

# mainThread1.join()
# mainThread2.join()
# mainThread3.join()
mainThread4.join()
speak("My Self Destruct has been initiated.")
selfDestruction(0)