import time
from utils import get_active_window, is_distracting
from notifier import show_reminder
from gpt_helper import generate_motivation_message

DISTRACTION_LIMIT = 5
DISTRACTING_KEYWORDS = ['YouTube', 'Netflix', 'Instagram', 'Discord']

distracted_start = None

print("🔍 Focus Guardian Agent started...")

while True:
    title = get_active_window()
    if is_distracting(title, DISTRACTING_KEYWORDS):
        if not distracted_start:
            distracted_start = time.time()
        elif time.time() - distracted_start > DISTRACTION_LIMIT:
            print("⚠️ Detected distraction: ", title)
            print("💡 " + generate_motivation_message())
            show_reminder("⚠️ You’re distracted! Focus now!")
            distracted_start = None
    else:
        distracted_start = None
    time.sleep(2)
