import subprocess
from Barbara import speak, lis

def set_alarm(query):
    speak('What time do you want to set the alarm for?')
    alarm_time = lis()
    if 'set alarm' in query:
        try:
            command = f"New-ScheduledTaskTrigger -Once -At {alarm_time} ; Register-ScheduledTask -Trigger $_ -TaskName 'MyAlarm'"
            subprocess.run(["powershell", "-Command", command])
            speak(f"Alarm set for {alarm_time}.")
        except Exception as e:
            speak("Sorry, I couldn't set the alarm. Please try again")

def delete_alarm(query):
    