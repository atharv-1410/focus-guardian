from plyer import notification
from gpt_helper import generate_motivation_message

def show_reminder(msg):
    ant = generate_motivation_message()
    print(ant)
    notification.notify(
        title="Focus Guardian",
        message=msg + "\n\n" + ant,  # includes motivational message in popup
        timeout=5
    )
