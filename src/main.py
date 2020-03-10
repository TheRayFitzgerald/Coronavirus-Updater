from datetime import datetime
import send_email

def daily_email():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time == "20:10":
        send_email.send_email()

if __name__ == '__main__':
    while(True):
        daily_email()