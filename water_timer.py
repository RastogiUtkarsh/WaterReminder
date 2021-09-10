#Timer Program
import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water",
            message="Water is more important than this!!",
            app_icon = "location of paani(water).ico"
            timeout=10
        )
        time.sleep(60*60)
