from datetime import datetime
from playsound import playsound

hour = int(input('Please, enter the hour of the alarm clock.'))
minutes = int(input('Please, enter the minutes of the alarm clock.'))
seconds = int(input('Please, enter the seconds of the alarm clock.'))

clock_type = input('AM or PM?').lower()

if clock_type == 'AM':
    hour = hour - 12
else:
    hour = hour + 12

while True:
    if datetime.now().hour == hour and datetime.now().minute == minutes and datetime.now().second == seconds:
        playsound('C:\\Users\\PC\\Downloads\\alarm_clock.mp3')
        break



