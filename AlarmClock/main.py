from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)  # will start after sec
        time_elapsed += 1 # every second, time elapsed will increase by one

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in : {minutes_left:02d} : {seconds_left:02d}")
                # :02d makes it as 2 digits and defaults to 0
    playsound("Timeless-Ringtone-RingRhythmic.com_.mp3")


minutes = int(input("How many minutes: "))
seconds = int(input("How many seconds: "))
total_secs = (minutes * 60) + seconds
alarm(total_secs)