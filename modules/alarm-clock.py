from os import system
from colorama import Fore as c
import sys
import time

def ask_redy_to_use():
    print(c.RED + """
Warning:Welcome to this tool! You know if set you end time and
dont do it I do some punishment so please ask this qoustion:""")
    user_answer = input("Are you sure to start?[Y/n]")

    if user_answer == "n" or "N":
        print(c.WHITE + "Press ctrl + c to exit")
    else:
        pass

def time_to_use():
    try:
        while True:
            time = int(input("Please enter your time to use:"))
            if time == None:
                print("Please enter a time :( or press Ctrl + c to exit")
                continue
            else:
                now = time.time()
                while True:
                    finsh_time = time.time()
                    if now + time == finsh_time:
                        system("play alarm_text.mp3")
                        print(c.GREEN + "You time is up!")
                    elif now + time > finsh_time:
                        print(c.RED + "Oh! Stop!")
                        time.sleep(2)
                        system("play alarm_text.mp3")
                    elif now + time > finsh_time + 20:
                        print(c.RED + "So, I shutdown you system.")
                        system("shutdown")
    except Exception as err:
        pass

if __name__ == '__main__':
    ask_redy_to_use()
    time_to_use()
