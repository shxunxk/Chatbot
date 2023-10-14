import time
import threading
import datetime
from Barbara import speak, lis

alarm_timer = None

def set_alarm(query):
    global alarm_timer
    if 'set alarm' in query:
        speak("What time would you like to set the alarm for? Please specify the time in HH:MM format.")
        alarm_time = lis()
        try:
            alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
            now = datetime.datetime.now()
            alarm_datetime = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
            if alarm_datetime <= now:
                alarm_datetime += datetime.timedelta(days=1)
            time_difference = (alarm_datetime - now).total_seconds()
            if alarm_timer is not None:
                alarm_timer.cancel()
            alarm_timer = threading.Timer(time_difference, alarm_callback)
            alarm_timer.start()
            speak(f"Alarm set for {alarm_time}.")
        except ValueError:
            speak("Sorry, I couldn't understand the time. Please specify the time in HH:MM format.")

def delete_alarm(query):
    global alarm_timer
    if 'delete alarm' in query:
        speak("Are you sure you want to delete the alarm? (Yes or No)")
        response = lis()
        if response.lower() == "yes":
            if alarm_timer is not None:
                alarm_timer.cancel()
                alarm_timer = None
                speak("The alarm has been deleted.")
            else:
                speak("There is no active alarm to delete.")
        else:
            speak("The alarm has not been deleted.")