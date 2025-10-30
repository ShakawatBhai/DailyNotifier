from plyer import notification # type: ignore
import schedule # type: ignore
import time
import threading

def send_notification(title, message):
    """Display desktop notification"""
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

def schedule_notification(time_str, title, message, repeat_daily=True):
    """Schedule notification at given time"""
    schedule.clear()  # clear previous jobs

    if repeat_daily:
        schedule.every().day.at(time_str).do(send_notification, title, message)
    else:
        schedule.every().day.at(time_str).do(
            lambda: [send_notification(title, message), schedule.clear()]
        )

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run_schedule, daemon=True)
    thread.start()
