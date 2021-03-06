from gtts import gTTS
import time
from colorama import Fore as c

while True:
    try:
        user_alarm = input(c.WHITE + "Please enter your text alarm:")
        if user_alarm == None:
            print(c.RED + "Please enter your text!")
            continue
        else:
            break
    except Exception as err:
        print(c.RED + "E:" + err)

try:
    alarm_voice = gTTS(user_alarm)
    alarm_voice.save("alarm-text.mp3")
    print("Proccessing text to speech . . .")
    time.sleep(3)
except Exception as err:
    print(c.RED + "E:" + err)

print(c.GREEN + "\nText to speech successfuly save!")
